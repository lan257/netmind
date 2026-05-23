# Skill 修改指南

## 功能说明

本 Skill 指导 Agent 修改已有 prompt-only Skill。修改目标是让一个 Skill 文件夹内的提示、流程和维护说明保持一致，同时守住 Skill 与 Tool 的边界。

## 触发场景

- 用户要求修改已有 Skill 的提示或触发条件。
- 用户要求调整 Skill 的工作流、维护说明、分类或标签。
- 用户指出 Skill 文件夹内的定义和流程不一致。
- 用户想把某个 Skill 从“可执行能力”纠正为 prompt-only 能力。

## 修改规则

- 修改前只定位一个 Skill 文件夹，读取其中的 `skill_definition.json`、`workflow.md` 和 `maintenance.md`。
- 修改较长的 `skill.md`、`workflow.md` 或 `maintenance.md` 时，使用 `long_text_line_modifier_guide` 规划分块批量写入。
- 基本流程不手动编辑 `.skill/lists` 或绑定文件。
- 如果用户新增的是执行动作、参数、权限或脚本逻辑，应转为 Tool 修改或 Tool 创建。
- 不要在 Skill 目录新增 `run.py`。
- 不要在 Skill 定义中加入 Tool 字段。

## 基本流程

1. 定位待修改的 Skill 文件夹。
2. 读取三件套，理解当前触发条件、提示目标、流程和维护边界。
3. 判断用户变更是否仍属于 prompt-only。
4. 修改受影响文件。
5. 写入较长文本时按 `long_text_line_modifier_guide` 分块批量写入。
6. 校验三件套完整、定义一致、无可执行字段、无 `run.py`。
7. 输出修改摘要、校验结果和剩余风险。

## 验收清单

- 一个 Skill 只修改一个文件夹。
- `workflow.md` 与 `prompt` 的目标一致。
- `maintenance.md` 反映新的维护边界。
- Skill 文件夹下没有 `run.py`。
- 没有把 Tool 的参数、权限或脚本路径写入 Skill。
- 没有手动编辑 `.skill/lists` 或绑定文件。
