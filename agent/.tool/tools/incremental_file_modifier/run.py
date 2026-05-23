import sys
import json
import os

def main():
    try:
        input_data = json.loads(sys.stdin.read())
        file_path = input_data.get("file_path")
        text = input_data.get("text")
        if not file_path or text is None:
            raise ValueError("缺少必要参数: file_path 和 text")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(text)
        result = {
            "success": True,
            "file_path": file_path,
            "appended": True,
            "length": len(text)
        }
    except Exception as e:
        result = {
            "success": False,
            "error": str(e)
        }
    print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    main()
