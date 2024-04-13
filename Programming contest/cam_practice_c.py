counts = int(input())

for a in range(counts):
    amount = 0
    ranges = list(map(int, input().split()))
    S = ranges[0]
    F = ranges[1]
    C = ranges[2]

    for i in range(S, F+1):
        for num in str(i):
            if num == str(C):
                amount += 1
    print(amount)