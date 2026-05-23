# Tool 创建流程

1. 判断用户需求是否需要执行动作；如果只需要提示流程，改用 Skill 创建流程。
2. 设计 `tool_id`，使用小写字母、数字和下划线，只创建一个 Tool 文件夹。
3. 明确参数表、权限级别、权限确认文案、返回结构和失败行为。
4. 编写 `run.py`，确保入口、参数读取、错误处理和返回值真实可用。
5. 编写 `tool_definition.json`，声明 `tool_id`、`tool_name`、`description`、`trigger`、`params`、`permission_level`、`permission_message`、`script_path`、`category`、`tags`。
6. 编写 `tool.md`，覆盖功能、参数、返回值、示例、安全限制和维护说明。
7. 写入较长的 `run.py` 或 `tool.md` 时，使用 `long_text_line_modifier_guide` 将内容拆成多次批量写入。
8. 校验当前 Tool 文件夹内的定义、脚本和文档一致。
9. 如有实现风险，补充针对 `run.py` 的单元测试或最小运行验证。
10. 输出 Tool 文件夹、验证结果和剩余风险。
