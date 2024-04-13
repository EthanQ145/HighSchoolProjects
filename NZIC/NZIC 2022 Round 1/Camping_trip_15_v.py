N, A, B = map(int, input().split())
temps = list(map(int, input().split()))
good = 0

for temp in temps:
    if A <= temp <= B:
        good += 2

if good != 0:
    print(good - 1)
elif good - 1 >= N:
    print(N)
else:
    print(0)
