# Tool 创建指南

## 功能说明

本 Skill 指导 Agent 创建 executable Tool。Tool 是可信的可执行能力，负责实际运行脚本、处理参数、读写文件、调用外部接口，并返回结构化结果。

Tool 与 Skill 的边界：

| 类型 | 存放位置 | 文件结构 | 适用场景 |
| --- | --- | --- | --- |
| Tool | 一个 Tool 文件夹 | `tool_definition.json`、`run.py`、`tool.md` | 可执行动作、文件操作、接口调用、脚本运行 |
| Skill | 一个 Skill 文件夹 | `skill_definition.json`、`workflow.md`、`maintenance.md` | 提示规范、工作流、判断标准、维护方法 |

## 触发场景

- 用户要新增可被 Agent 调用的动作能力。
- 用户要封装文件读写、系统查询、接口调用或数据处理。
- 用户描述了输入参数和期望运行结果。
- 用户要求创建 `run.py` 或脚本型能力。

## 创建规则

- 基本创建流程只维护一个 Tool 文件夹。
- 三件套必须完整：`tool_definition.json`、`run.py`、`tool.md`。
- `tool_definition.json` 必须包含 `params`、`permission_level`、`permission_message`、`script_path`。
- 规范 `script_path` 必须指向对应 Tool 目录下的 `run.py`。
- 不要手动编辑 `.tool/lists` 或把 Tool 做成 Skill。
- 写入较长的 `run.py` 或 `tool.md` 时，使用 `long_text_line_modifier_guide` 规划分块批量写入。

## 基本流程

1. 确认需求确实需要执行能力。
2. 设计 `tool_id`、参数、权限级别和返回结构。
3. 编写 `run.py`，实现真实逻辑和错误处理。
4. 编写 `tool_definition.json`，声明参数、权限、脚本路径、分类和标签。
5. 编写 `tool.md`，说明功能、参数、返回值、示例和维护事项。
6. 写入较长文本时按 `long_text_line_modifier_guide` 分块批量写入。
7. 校验该 Tool 文件夹内定义、实现和文档一致，必要时补测试。

## 验收清单

- 目录名与 `tool_id` 一致。
- `tool_definition.json`、`run.py`、`tool.md` 都存在。
- `script_path` 指向对应目录下的 `run.py`。
- `permission_message` 中的占位符都能在 `params` 中找到。
- 文档描述、参数定义和 `run.py` 实现一致。
- 一个 Tool 只对应一个文件夹。
- 没有手动编辑 `.tool/lists` 或绑定文件。
