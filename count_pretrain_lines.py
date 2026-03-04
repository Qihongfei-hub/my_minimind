import json
import random

# 文件路径
file_path = "dataset/pretrain_hq.jsonl"

# 读取所有行
with open(file_path, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

# 随机抽取50行
if len(lines) >= 50:
    sampled_lines = random.sample(lines, 50)
else:
    sampled_lines = lines
    print(f"文件行数不足50，仅抽取{len(lines)}行")

# 统计并打印结果
print("随机抽取的50行及其字数：")
print("-" * 80)
for i, line in enumerate(sampled_lines, 1):
    try:
        # 解析JSON
        data = json.loads(line)
        # 提取text字段的字数
        if 'text' in data:
            total_chars = len(data['text'])
            print(f"第{i}行：{total_chars} 字")
        else:
            print(f"第{i}行：无text字段")
    except json.JSONDecodeError:
        print(f"第{i}行：JSON解析失败")
print("-" * 80)