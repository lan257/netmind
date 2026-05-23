"""Backward-compatible registry imports.

New code should import executable Tool loading from `tool_registry` and
prompt-only Skill loading from `skill_registry`.
"""

from __future__ import annotations

from pathlib import Path

from .registry_utils import load_yaml_like as _load_yaml_like
from .registry_utils import split_key_value as _split_key_value
from .schemas import PromptSkillDefinition, SkillDefinition, ToolDefinition
from .skill_registry import (
    SKILL_ROOT,
    load_prompt_skill_definitions,
    summarize_prompt_skills,
    validate_prompt_skill_tree,
)
from .tool_registry import (
    TOOL_ROOT,
    load_domain_bindings,
    load_skill_definitions,
    load_tool_definitions,
    summarize_skills,
    summarize_tools,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


__all__ = [
    "PROJECT_ROOT",
    "TOOL_ROOT",
    "SKILL_ROOT",
    "PromptSkillDefinition",
    "SkillDefinition",
    "ToolDefinition",
    "load_domain_bindings",
    "load_tool_definitions",
    "load_skill_definitions",
    "load_prompt_skill_definitions",
    "summarize_tools",
    "summarize_skills",
    "summarize_prompt_skills",
    "validate_prompt_skill_tree",
    "_load_yaml_like",
    "_split_key_value",
]
