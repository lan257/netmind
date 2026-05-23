"""Legacy SkillCall compatibility wrapper for ToolCall rebuilding."""

from __future__ import annotations

from typing import Any

from .compat import add_legacy_skill_call_aliases, normalize_tool_call_draft, normalize_tool_call_record
from .schemas import SkillDefinition
from .tool_call_builder import (
    merge_permission_result as merge_tool_permission_result,
    rebuild_tool_call_records,
    split_executable_tool_calls,
)


def rebuild_skill_call_records(
    drafts: list[dict[str, Any]],
    skill_definitions: list[SkillDefinition],
    turn_id: str | None = None,
) -> list[dict[str, Any]]:
    """Convert legacy Skill drafts into ToolCallRecords with legacy aliases."""
    tool_drafts = [normalize_tool_call_draft(draft) for draft in drafts]
    records = rebuild_tool_call_records(tool_drafts, skill_definitions, turn_id=turn_id)
    return [add_legacy_skill_call_aliases(record) for record in records]


def merge_permission_result(
    history_skill_calls: list[dict[str, Any]],
    confirmed_skill_calls: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Merge legacy permission decisions into previous call records."""
    history = [normalize_tool_call_record(record) for record in history_skill_calls]
    confirmed = [normalize_tool_call_record(record) for record in confirmed_skill_calls]
    records = merge_tool_permission_result(history, confirmed)
    return [add_legacy_skill_call_aliases(record) for record in records]


def split_executable_skill_calls(
    skill_calls: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Split ready legacy SkillCallRecords from records returned as-is."""
    tool_calls = [normalize_tool_call_record(record) for record in skill_calls]
    executable, pending = split_executable_tool_calls(tool_calls)
    return (
        [add_legacy_skill_call_aliases(record) for record in executable],
        [add_legacy_skill_call_aliases(record) for record in pending],
    )
