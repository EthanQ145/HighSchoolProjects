available_points = int(input())
skills = sorted(list(map(int, input().split())))
attack = 0

accuracy = 0

for points in range(available_points):
    if attack <= accuracy:
        attack += skills[-1]
        skills.remove(skills[-1])
    elif accuracy < attack:
        accuracy += skills[-1]
        if accuracy > 100:
            if attack * 100 < (attack + skills[-1]) * (accuracy - skills[-1]):
                attack += skills[-1]
                accuracy -= skills[-1]
        skills.remove(skills[-1])

if accuracy > 100:
    print(attack * 100)
else:
    print(attack * accuracy)


