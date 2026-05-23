"""API boundary adapters for new tool_* fields and legacy skill_* callers."""

from __future__ import annotations

from typing import Any

from .compat import add_legacy_skill_call_aliases, normalize_tool_call_record


API_V1 = "v1"
API_V2 = "v2"
SUPPORTED_API_VERSIONS = {API_V1, API_V2}


def normalize_request_payload(raw_request: dict[str, Any] | None) -> dict[str, Any]:
    """Normalize inbound API payloads before they enter kernel internals."""
    raw = dict(raw_request or {})
    normalized = dict(raw)
    normalized["api_version"] = normalize_api_version(raw.get("api_version"))
    if "domain" not in normalized and raw.get("domain_and_skill_binding") is not None:
        normalized["domain"] = raw["domain_and_skill_binding"]
    normalized.setdefault("domain", "default")
    if "tool_runtime" not in normalized:
        normalized["tool_runtime"] = _read_legacy_runtime(raw)
    normalized["history_tool_calls"] = [
        normalize_tool_call_record(item)
        for item in _read_call_list(raw, "history_tool_calls", "history_skill_calls")
    ]
    normalized["confirmed_tool_calls"] = [
        normalize_tool_call_record(item)
        for item in _read_call_list(raw, "confirmed_tool_calls", "confirmed_skill_calls")
    ]
    return normalized


def build_api_response(
    core_response: dict[str, Any],
    include_legacy: bool = True,
    api_version: str = API_V1,
) -> dict[str, Any]:
    """Adapt the internal Tool response to the public API shape."""
    response = dict(core_response)
    response["api_version"] = normalize_api_version(api_version)
    tool_calls = [
        normalize_tool_call_record(item)
        for item in response.get("tool_calls", [])
        if isinstance(item, dict)
    ]
    response["tool_calls"] = tool_calls
    if include_legacy:
        response["skill_calls"] = [add_legacy_skill_call_aliases(item) for item in tool_calls]
    return response


def normalize_api_version(value: Any) -> str:
    """Return a supported API version, defaulting to the v1 compatibility contract."""
    version = str(value or API_V1).strip().lower()
    if version not in SUPPORTED_API_VERSIONS:
        raise ValueError(f"unsupported api_version: {value}")
    return version


def should_include_legacy_fields(api_version: str) -> bool:
    """Only API v1 exposes legacy skill_* aliases."""
    return normalize_api_version(api_version) == API_V1


def _read_legacy_runtime(raw: dict[str, Any]) -> dict[str, Any]:
    runtime = raw.get("skill_runtime")
    if runtime is None:
        runtime = raw.get("runtime_params")
    if runtime is None:
        runtime = raw.get("client_params")
    return dict(runtime or {})


def _read_call_list(raw: dict[str, Any], current_key: str, legacy_key: str) -> list[dict[str, Any]]:
    value = raw.get(current_key)
    if value is None:
        value = raw.get(legacy_key)
    if not isinstance(value, list):
        return []
    return [dict(item) for item in value if isinstance(item, dict)]
