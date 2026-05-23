# Tool 修改指南

## 功能说明

本 Skill 指导 Agent 修改已有 executable Tool。修改时只维护一个 Tool 文件夹，同时关注实现、定义、文档和权限，避免出现“文档说有、脚本没有”或“参数变了、实现没跟上”的问题。

## 触发场景

- 用户要求修改已有 Tool 的功能或脚本逻辑。
- 用户要求新增、删除或重命名 Tool 参数。
- 用户要求调整权限级别、权限提示或安全限制。
- 用户指出 Tool 文档、定义和实现不一致。
- 用户要求修改 Tool 的分类或标签。

## 修改规则

- 修改前只定位一个 Tool 文件夹，读取其中的 `tool_definition.json`、`run.py` 和 `tool.md`。
- 修改较长的 `run.py` 或 `tool.md` 时，使用 `long_text_line_modifier_guide` 规划分块批量写入。
- 参数变化必须同步 `params`、`permission_message`、`run.py` 和 `tool.md`。
- 权限变化必须同步定义、文档和必要的测试。
- 基本流程不手动编辑 `.tool/lists` 或绑定文件。
- 不要把 Tool 改成只有 prompt 的空壳；如果不再需要执行能力，应迁移为 Skill。

## 基本流程

1. 定位待修改的 Tool 文件夹。
2. 读取三件套，理解当前参数、权限、实现和文档。
3. 判断用户变更会影响哪些文件。
4. 修改 `run.py` 的真实逻辑。
5. 同步修改 `tool_definition.json` 和 `tool.md`。
6. 写入较长文本时按 `long_text_line_modifier_guide` 分块批量写入。
7. 校验该 Tool 文件夹内定义、脚本和文档一致，并运行必要测试。
8. 输出修改摘要、验证结果和剩余风险。

## 验收清单

- 一个 Tool 只修改一个文件夹。
- `run.py` 实现了文档和定义声明的能力。
- `params` 与 `run.py` 的参数读取一致。
- `permission_message` 占位符都存在于 `params`。
- `tool.md` 的示例和返回值仍然准确。
- `script_path` 仍指向对应 Tool 的 `run.py`。
- 没有手动编辑 `.tool/lists` 或绑定文件。
