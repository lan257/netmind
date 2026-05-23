# 维护说明

- Tool 是可执行能力，必须维护 `tool_definition.json`、`run.py` 和 `tool.md`，不要做成 Skill。
- `run.py` 必须实现 `tool_definition.json` 和 `tool.md` 声明的能力，不能只有占位逻辑。
- 修改参数时同步更新定义、文档、权限文案、实现和测试。
- 高风险操作使用 `confirm` 或 `high` 权限，不要默认 `none`。
- `permission_message` 里的 `{name}` 占位符必须来自 `params`。
- 基本流程不直接写 `.tool` 列表或绑定文件。
- 长文本写入使用 `long_text_line_modifier_guide` 拆块，避免超出单次文件编辑限制。
