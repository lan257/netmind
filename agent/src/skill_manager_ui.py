"""Compatibility wrapper for the Tool/Skill manager web UI.

The implementation lives in `tools.skill_manger.skill_manager_ui`.
"""

from __future__ import annotations

from tools.skill_manger.skill_manager_ui import *  # noqa: F401,F403
from tools.skill_manger.skill_manager_ui import main


if __name__ == "__main__":
    raise SystemExit(main())
