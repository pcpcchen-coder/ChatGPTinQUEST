import importlib.util
import os
from pathlib import Path
import tempfile
import tomllib
import unittest

spec = importlib.util.spec_from_file_location(
    "setup", Path(__file__).parents[1] / "scripts/configure_mcp.py")
setup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup)


class ConfigureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.config = self.root / "config.toml"
        self.uvx = self.root / 'space folder' / 'uvx'
        self.uvx.parent.mkdir()
        self.uvx.write_text("#!/bin/sh\nexit 0\n")
        self.uvx.chmod(0o700)

    def run_setup(self):
        return setup.configure(self.config, str(self.uvx))

    def test_new_and_idempotent(self):
        self.run_setup()
        before = self.config.read_bytes()
        self.run_setup()
        self.assertEqual(before, self.config.read_bytes())
        parsed = tomllib.loads(before.decode())
        self.assertEqual(parsed['mcp_servers']['figmin-xr']['command'], str(self.uvx))
        self.assertEqual(self.config.stat().st_mode & 0o777, 0o600)

    def test_preserve_existing_and_private_backup(self):
        original = b'# keep comment\nmodel = "existing"\n[mcp_servers.other]\ncommand = "other"\n'
        self.config.write_bytes(original)
        self.run_setup()
        self.assertTrue(self.config.read_bytes().startswith(original))
        backups = list(self.root.glob('config.toml.before-quest-*'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), original)
        self.assertEqual(backups[0].stat().st_mode & 0o777, 0o600)

    def test_conflict_untouched(self):
        original = '[mcp_servers.figmin-xr]\ncommand = "custom"\n'
        self.config.write_text(original)
        with self.assertRaises(ValueError):
            self.run_setup()
        self.assertEqual(self.config.read_text(), original)

    def test_invalid_toml_untouched(self):
        self.config.write_text('invalid = [')
        with self.assertRaises(tomllib.TOMLDecodeError):
            self.run_setup()
        self.assertEqual(self.config.read_text(), 'invalid = [')
        self.assertEqual(list(self.root.glob('config.toml.before-quest-*')), [])

    def test_inline_table_refused_without_changes(self):
        self.config.write_text('mcp_servers = {}\n')
        with self.assertRaises(tomllib.TOMLDecodeError):
            self.run_setup()
        self.assertEqual(self.config.read_text(), 'mcp_servers = {}\n')

    def test_symlink_refused(self):
        target = self.root / 'target.toml'
        target.write_text('# original')
        self.config.symlink_to(target)
        with self.assertRaises(ValueError):
            self.run_setup()
        self.assertEqual(target.read_text(), '# original')

    def test_disabled_entry_not_claimed_ready(self):
        self.config.write_text('[mcp_servers.figmin-xr]\ncommand = "uvx"\nargs = ["figmin-mcp"]\nenabled = false\n')
        before = self.config.read_bytes()
        with self.assertRaises(ValueError):
            self.run_setup()
        self.assertEqual(self.config.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
