import sys

# 从标准输入读取数据
input_data = sys.stdin.read()

# 在控制台输出接收到的数据
print("Python 接收到数据:", input_data)

# 对接收到的数据进行处理（示例：将接收到的数据转换为大写）
input_data+=" I am added from python"
output_data = input_data.upper()


# 将处理结果发送回 Node.js
sys.stdout.write(output_data)