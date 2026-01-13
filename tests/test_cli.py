from acon_ai_tools import __version__
from acon_ai_tools.cli import build_parser


def test_build_parser_has_commands():
    parser = build_parser()
    actions = [action for action in parser._actions if action.dest == "command"]
    assert actions, "command subparser should exist"


def test_version_is_string():
    assert isinstance(__version__, str)
