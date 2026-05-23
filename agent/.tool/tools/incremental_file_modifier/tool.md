# incremental_file_modifier - 增量文件修改器

## 功能
仅允许在指定文件最后面进行增量添加文本，不修改已有内容。权限级别为none，无需确认。

## 参数
- file_path (string, 必需): 要修改的目标文件路径（绝对路径）
- text (string, 必需): 要追加到文件末尾的文本内容

## 返回值
- success (bool): 操作是否成功
- file_path (string): 目标文件路径
- appended (bool): 是否已追加
- length (int): 追加的文本长度
- error (string, 可选): 错误信息

## 示例
```json
{
  "file_path": "/path/to/file.txt",
  "text": "追加的内容"
}
```

## 安全限制
- 仅追加，不修改已有内容
- 权限: none

## 维护说明
- 确保run.py脚本正确读取stdin的JSON参数
- 文件不存在时会自动创建父目录
- 修改tool_definition.json时需同步更新此文档
