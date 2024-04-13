num_count = input()
for i in range(int(num_count)):
    s, f, c = input().split()

    num_things = 0
    for f in range(int(s), int(f) + 1):
        if c in str(f):
            num_things += str(f).count(c)

    print(num_things)