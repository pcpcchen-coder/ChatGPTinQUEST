#!/usr/bin/env python3
"""Add Figmin MCP without rewriting existing TOML. Requires Python 3.11+."""
import argparse
import json
import os
from pathlib import Path
import tempfile
import tomllib


def configure(path: Path, uvx: str) -> str:
    if not Path(uvx).is_absolute() or not os.access(uvx, os.X_OK):
        raise ValueError("uvx 必須是存在且可執行的絕對路徑")
    if path.is_symlink():
        raise ValueError("設定檔是符號連結；請由本機 Agent 檢查後設定，避免替換連結")
    exists = path.exists()
    original = path.read_bytes() if exists else b""
    # Parse before touching anything. Never print config contents or secrets.
    parsed = tomllib.loads(original.decode("utf-8"))
    servers = parsed.get("mcp_servers", {})
    if not isinstance(servers, dict):
        raise ValueError("mcp_servers 格式錯誤，未修改設定")
    if "figmin-xr" in servers:
        entry = servers["figmin-xr"]
        if (isinstance(entry, dict)
                and entry.get("command") in (uvx, "uvx")
                and entry.get("args") == ["figmin-mcp"]
                and entry.get("enabled", True) is True
                and "url" not in entry):
            return "已存在 Figmin MCP 設定；保留原設定。請在客戶端驗證工具能否載入。"
        raise ValueError("figmin-xr 已存在不同或停用的設定；保留原檔，請本機 Agent 檢查")
    # Inline tables cannot be extended using a new TOML table; validate first.
    added = ("\n\n# ChatGPTinQUEST: first demo\n[mcp_servers.figmin-xr]\n"
             f"command = {json.dumps(uvx, ensure_ascii=False)}\n"
             'args = ["figmin-mcp"]\n')
    updated = original + added.encode("utf-8")
    tomllib.loads(updated.decode("utf-8"))
    path.parent.mkdir(parents=True, exist_ok=True)
    backup = None
    if exists:
        fd, name = tempfile.mkstemp(prefix="config.toml.before-quest-", dir=path.parent)
        backup = Path(name)
        with os.fdopen(fd, "wb") as f:
            f.write(original)
    fd, name = tempfile.mkstemp(prefix=".quest-config-", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(updated)
            f.flush()
            os.fsync(f.fileno())
        if path.exists() != exists or (exists and path.read_bytes() != original):
            raise ValueError("設定在處理期間有變更，未覆寫；請重新執行")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)
    return f"MCP 設定已加入。備份：{backup or '原本沒有設定檔'}。請重新啟動 AI 客戶端。"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uvx", required=True)
    args = parser.parse_args()
    config_root = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    try:
        print(configure(config_root / "config.toml", args.uvx))
    except (ValueError, OSError) as exc:
        # TOML parse errors can include private strings: do not echo them.
        if isinstance(exc, tomllib.TOMLDecodeError):
            print("設定 TOML 無法解析或擴充；原設定未修改，請本機 Agent 檢查。")
        else:
            print(f"設定未完成：{exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
