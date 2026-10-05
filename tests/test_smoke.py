"""Smoke test for demo target."""

from demo_target.cli import format_quiet_output


def test_format_verbose():
    assert format_quiet_output("hello", quiet=False) == "hello"
