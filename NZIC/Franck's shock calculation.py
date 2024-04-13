target = int(input())
num_shock = list(int(num) for num in input().split())
sym_shock = input().split()
symbol_dict = {"+": int(sym_shock[0]),
               "*": int(sym_shock[1]),
               "=": int(sym_shock[2])}
answer = []

# addition only
if target <= 9:
    answer.append(num_shock[target])

if target <= 18:
    for i in range(len(num_shock)):
        if (target - i) <= 9:
            answer.append(num_shock[i] + num_shock[target - i] + symbol_dict[
                "+"])

# multiplication
for i in range(1, len(num_shock)):
    if str(target / i)[-1] == "0" and target / i < 10:
        answer.append(num_shock[i] + num_shock[int(target / i)] +
                      symbol_dict["*"])

# both
for i in range(len(num_shock)):
    new_num = target - i
    for j in range(1, len(num_shock)):
        if str(new_num / j)[-1] == "0" and new_num / j < 10:
            answer.append(num_shock[i] + num_shock[int(new_num / j)] +
                          num_shock[j] + symbol_dict["*"] + symbol_dict["+"],)

print(min(answer) + symbol_dict["="])
