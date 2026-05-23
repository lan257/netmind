"""Legacy Skill execution wrapper around the Tool runner."""

from __future__ import annotations

from typing import Any

from .compat import add_legacy_skill_call_aliases, normalize_tool_call_record
from .tool_runner import execute_ready_tool_calls


def execute_ready_skill_calls(
    skill_calls: list[dict[str, Any]],
    skill_runtime: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Execute approved legacy SkillCallRecord entries."""
    tool_calls = [normalize_tool_call_record(record) for record in skill_calls]
    records = execute_ready_tool_calls(tool_calls, skill_runtime)
    return [add_legacy_skill_call_aliases(record) for record in records]
