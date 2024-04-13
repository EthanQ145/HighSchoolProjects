num_players = int(input())
skills = sorted(list(map(int, input().split())))
teams = []
for times in range(int(num_players/2)):
    teams.append(sum([skills[-1], skills[0]]))
    skills.remove(skills[-1])
    skills.remove(skills[0])

print(max(teams) - min(teams))
