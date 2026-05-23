"""Compatibility helpers between legacy skill_* and current tool_* protocol."""

from __future__ import annotations

from typing import Any


def normalize_tool_call_draft(draft: dict[str, Any]) -> dict[str, Any]:
    """Return a draft that uses tool_id internally."""
    normalized = dict(draft)
    if "tool_id" not in normalized and "skill_id" in normalized:
        normalized["tool_id"] = normalized["skill_id"]
    normalized.pop("skill_id", None)
    return normalized


def normalize_tool_call_record(record: dict[str, Any]) -> dict[str, Any]:
    """Return a ToolCallRecord-shaped mapping for internal processing."""
    normalized = dict(record)
    if "tool_id" not in normalized and "skill_id" in normalized:
        normalized["tool_id"] = normalized["skill_id"]
    if "tool_name" not in normalized and "skill_name" in normalized:
        normalized["tool_name"] = normalized["skill_name"]
    normalized.pop("skill_id", None)
    normalized.pop("skill_name", None)
    normalized["params"] = dict(normalized.get("params") or {})
    normalized["permission"] = dict(normalized.get("permission") or {})
    normalized["execution"] = dict(normalized.get("execution") or {})
    normalized["definition"] = dict(normalized.get("definition") or {})
    _normalize_diagnostics_to_tool_fields(normalized["execution"])
    return normalized


def add_legacy_skill_call_aliases(record: dict[str, Any]) -> dict[str, Any]:
    """Add legacy skill_* aliases for API v1 callers."""
    aliased = dict(record)
    if "skill_id" not in aliased and "tool_id" in aliased:
        aliased["skill_id"] = aliased["tool_id"]
    if "skill_name" not in aliased and "tool_name" in aliased:
        aliased["skill_name"] = aliased["tool_name"]
    if isinstance(aliased.get("execution"), dict):
        aliased["execution"] = dict(aliased["execution"])
        _add_legacy_diagnostic_aliases(aliased["execution"])
    return aliased


def add_legacy_skill_call_draft_aliases(draft: dict[str, Any]) -> dict[str, Any]:
    """Add a legacy skill_id alias to a model draft."""
    aliased = dict(draft)
    if "skill_id" not in aliased and "tool_id" in aliased:
        aliased["skill_id"] = aliased["tool_id"]
    return aliased


def _normalize_diagnostics_to_tool_fields(execution: dict[str, Any]) -> None:
    diagnostics = execution.get("diagnostics")
    if not isinstance(diagnostics, dict):
        return
    if "failed_tool_id" not in diagnostics and "failed_skill_id" in diagnostics:
        diagnostics["failed_tool_id"] = diagnostics["failed_skill_id"]


def _add_legacy_diagnostic_aliases(execution: dict[str, Any]) -> None:
    diagnostics = execution.get("diagnostics")
    if not isinstance(diagnostics, dict):
        return
    if "failed_skill_id" not in diagnostics and "failed_tool_id" in diagnostics:
        diagnostics["failed_skill_id"] = diagnostics["failed_tool_id"]
