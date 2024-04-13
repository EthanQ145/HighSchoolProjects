N = int(input())
num = int(input())
tools = ["+", "-", "*"]

for i in range(N-1):
    second_num = int(input())
    if tools[0] == "+":
        num += second_num
        tools.pop(0)
        tools.append("+")
    elif tools[0] == "-":
        num -= second_num
        tools.pop(0)
        tools.append("-")
    elif tools[0] == "*":
        num *= second_num
        tools.pop(0)
        tools.append("*")

print(num)