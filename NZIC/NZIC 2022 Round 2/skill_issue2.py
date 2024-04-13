available_points = int(input())
skills = sorted(list(map(int, input().split())))
attack = 0

accuracy = 0
if sum(skills) > 200:
    largest_attack = 0
    for skill in skills:
        largest_attack = max()
else:
    if attack <= accuracy:
        attack += skills[-1]
        skills.remove(skills[-1])
    elif accuracy < attack:
        accuracy += skills[-1]
        skills.remove(skills[-1])
    print(attack * accuracy)