"""Compatibility wrapper for the Tool/Skill manager CLI.

The implementation lives in `tools.skill_manger.skill_manager`.
"""

from __future__ import annotations

from tools.skill_manger.skill_manager import *  # noqa: F401,F403
from tools.skill_manger.skill_manager import main


if __name__ == "__main__":
    raise SystemExit(main())
