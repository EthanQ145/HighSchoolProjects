ducks_can_give = int(input())
all_ducks = input().split()
r_ducks = int(all_ducks[0])
p_ducks = int(all_ducks[1])
d_ducks = int(all_ducks[2])

g_ducks = int(all_ducks[-1])
total = r_ducks + p_ducks + d_ducks + g_ducks
ducks_wanted = input()

ducks_gave_away = 0
r_wanted = 0
p_wanted = 0
d_wanted = 0

for duck_wanted in ducks_wanted:
    if duck_wanted == 'R':
        r_wanted += 1
    elif duck_wanted == 'P':
        p_wanted += 1
    else:
        d_wanted += 1
r_leftover = r_ducks - r_wanted
p_left_over = p_ducks - p_wanted
d_left_over = d_ducks - d_wanted


for duck_wanted in ducks_wanted:
    if duck_wanted == 'R':
        r_ducks -= 1
    elif duck_wanted == 'P':
        p_ducks -= 1
    elif duck_wanted == 'D':
        d_ducks -= 1

if r_ducks == max(r_ducks, p_ducks, d_ducks):
    most_ducks = r_ducks
elif p_ducks == max(r_ducks, p_ducks, d_ducks):
    print('gave away p')
    p_ducks -= 1
else:
    print('gave away d')
    d_ducks -= 1



print(ducks_gave_away)
print(total - ducks_gave_away)
