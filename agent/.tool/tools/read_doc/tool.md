# read_doc

## SkillDefinition
该 Skill 的规范定义维护在同目录的 `skill_definition.json` 中；角色列表里的登记必须与该 JSON 完全一致。

```yaml
skill_id: read_doc
skill_name: 文件读取
description: 读取指定文件内容
trigger: 当需要读取文件内容时使用
params:
  filepath: string
permission_level: confirm
permission_message: 是否允许读取 {filepath}
script_path: .skill/skills/read_doc/run.py
```

## 功能
读取指定文本文件内容，供 Agent Kernel 后续总结或分析使用。

## 参数
- `filepath`: 需要读取的文件路径。

## 返回值
- `content`: 文件内容。
- `filepath`: 实际读取路径。

## 异常
文件不存在、路径不是文件或读取失败时，脚本抛出异常，由 Kernel 统一转换为 Skill 执行失败结果。
