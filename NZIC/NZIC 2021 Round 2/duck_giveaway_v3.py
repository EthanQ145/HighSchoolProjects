ducks_can_give = int(input())
all_ducks = input().split()
r_ducks = int(all_ducks[0])
p_ducks = int(all_ducks[1])
d_ducks = int(all_ducks[2])

g_ducks = int(all_ducks[-1])
total = r_ducks + p_ducks + d_ducks + g_ducks
ducks_wanted = list(input())

ducks_gave_away = 0

r_leftover = r_ducks - ducks_wanted.count('R')
p_leftover = p_ducks - ducks_wanted.count('P')
d_leftover = d_ducks - ducks_wanted.count('D')

while ducks_can_give > 0:
    if ducks_wanted[0] == 'R':
        if r_ducks == 0:
            break
        r_ducks -= 1
        r_leftover -= 1
    elif ducks_wanted[0] == 'P':
        if p_ducks == 0:
            break
        p_ducks -= 1
        p_leftover -= 1
    elif ducks_wanted[0] == 'D':
        if d_ducks == 0:
            break
        d_ducks -= 1
        d_leftover -= 1
    elif ducks_wanted[0] == 'G':
        if g_ducks == 0:
            break
        g_ducks -= 1
    else:
        if r_leftover == max(r_leftover, p_leftover, d_leftover):
            if r_ducks == 0:
                break
            r_ducks -= 1
            r_leftover -= 1
        elif p_leftover == max(r_leftover, p_leftover, d_leftover):
            if p_ducks == 0:
                break
            p_ducks -= 1
            p_leftover -= 1
        else:
            if d_ducks == 0:
                break
            d_ducks -= 1
            d_leftover -= 1
    ducks_wanted.pop(0)

    ducks_gave_away += 1


print(ducks_gave_away)
print(total - ducks_gave_away)
