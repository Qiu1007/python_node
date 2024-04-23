import sys


# input_data = sys.stdin.read()


# print("Python receive data:", input_data)


# input_data+=" I am added from python"
# output_data = input_data.upper()
# print("哈哈")
import json
sys.stdout.reconfigure(encoding='utf-8')

dicts={"b":"哈哈","k":0}
jsonStr = json.dumps(dicts, ensure_ascii=False)
sys.stdout.write(jsonStr)

