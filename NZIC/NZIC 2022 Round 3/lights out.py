lights = int(input())
ppl = int(input())
corridor = []


for i in range(lights):
    corridor.append(1)

count = 0
for i in range(2, ppl + 1):
    count = 1
    for j in range(len(corridor)):
        if count == i:
            if corridor[j] == 1:
                corridor[j] = 0
            else:
                corridor[j] = 1
            count = 0
        count += 1

total = 0
for light in corridor:
    if light == 1:
        total += 1

print(total)
