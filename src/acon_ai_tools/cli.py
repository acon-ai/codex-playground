"""Command line interface for ACon AI automation tools."""

from __future__ import annotations

import argparse
import platform
from pathlib import Path


def _cmd_hello(_: argparse.Namespace) -> int:
    print("你好，ACon AI 自动化工具已准备就绪。")
    return 0


def _cmd_doctor(_: argparse.Namespace) -> int:
    cwd = Path.cwd()
    required_paths = ["src", "scripts", "tests"]
    status_lines = []
    for rel_path in required_paths:
        path = cwd / rel_path
        status_lines.append(f"- {rel_path}: {'存在' if path.exists() else '缺失'}")

    print("环境诊断:")
    print(f"- Python 版本: {platform.python_version()}")
    print(f"- 当前目录: {cwd}")
    print("- 关键目录状态:")
    for line in status_lines:
        print(line)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="acon_ai_tools",
        description="面向财务/税务/Excel/PDF 的自动化工具箱。",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    hello_parser = subparsers.add_parser("hello", help="输出欢迎信息")
    hello_parser.set_defaults(func=_cmd_hello)

    doctor_parser = subparsers.add_parser("doctor", help="输出环境诊断信息")
    doctor_parser.set_defaults(func=_cmd_doctor)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
