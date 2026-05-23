# 维护说明

- Skill 是 prompt-only 能力，不要把 `run.py`、权限配置或可执行参数放进 Skill 文件夹。
- 需要执行动作时，新建或修改 Tool 文件夹。
- `workflow.md` 只保存文本流程，不保存 JSON 对象或脚本实现。
- 基本流程不要直接维护 `.skill/lists` 或绑定文件。
- 写入长文本时不要塞进单次写入，使用 `long_text_line_modifier_guide` 拆成批量小块。
- 修改字段结构时，同步检查加载器、校验逻辑、管理 UI 和测试。
- 常见错误：把 Tool 的 `tool_definition.json`、`run.py`、`tool.md` 三件套复制成 Skill；这种情况应改用 Tool 创建或修改流程。
