# Skill 修改流程

1. 读取目标 Skill 的 `skill_definition.json`、`workflow.md` 和 `maintenance.md`。
2. 确认当前只修改这一个 Skill 文件夹。
3. 明确用户要修改的是触发条件、提示、流程、维护说明、分类还是标签。
4. 判断变更是否仍是 prompt-only；如果涉及执行代码、文件读写、外部接口或运行结果，转入 Tool 流程。
5. 修改目录内三件套中受影响的文件。
6. 写入较长的 `skill.md`、`workflow.md`、`maintenance.md` 时，使用 `long_text_line_modifier_guide` 拆成多次批量写入。
7. 校验目录内没有 `run.py`，定义中没有 `params`、`permission`、`script_path` 等 Tool 字段。
8. 输出更新摘要、校验结果和需要用户留意的风险。
