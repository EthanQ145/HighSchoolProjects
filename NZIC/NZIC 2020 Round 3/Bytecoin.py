days, initial = map(int, input().split())
buys = list(map(int, input().split()))
sells = list(map(int, input().split()))


for i in range(days):
    if i != days - 1:
        if buys[i] < sells[i+1]:
            initial = max(initial, initial % buys[i] + initial // buys[i] * sells[i + 1])
print(initial)


