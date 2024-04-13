ducks_can_give = int(input())
all_ducks = input().split()
r_ducks = int(all_ducks[0])
p_ducks = int(all_ducks[1])
d_ducks = int(all_ducks[2])

g_ducks = int(all_ducks[-1])
total = r_ducks + p_ducks + d_ducks + g_ducks
ducks_wanted = list(input())

ducks_gave_away = 0
r_wanted = 0
p_wanted = 0
d_wanted = 0
priority = []
for duck_wanted in ducks_wanted:
    if duck_wanted == 'R':
        r_wanted += 1
    elif duck_wanted == 'P':
        p_wanted += 1
    else:
        d_wanted += 1


while ducks_can_give > 0:
    if ducks_wanted[0] == 'R':
        if r_ducks == 0:
            break
        r_ducks -= 1
        r_wanted -= 1
    elif ducks_wanted[0] == 'P':
        if p_ducks == 0:
            break
        p_ducks -= 1
        p_wanted -= 1
    elif ducks_wanted[0] == 'D':
        if d_ducks == 0:
            break
        d_ducks -= 1
        d_wanted -= 1
    elif ducks_wanted[0] == 'G':
        if g_ducks == 0:
            break
        g_ducks -= 1
    else:
        ducks_wanted.pop(0)
        if r_wanted == min(r_wanted, p_wanted, d_wanted) and r_wanted > 0:
            print('CHose R')
            if r_ducks == 0:
                break
            r_ducks -= 1
            r_wanted -= 1
        elif p_wanted == min(r_wanted, p_wanted, d_wanted) and p_wanted > 0:
            print('CHose P')
            if p_ducks == 0:
                break
            p_ducks -= 1
            p_wanted -= 1
        else:
            print('CHose P')
            if d_ducks == 0:
                break
            d_ducks -= 1
            d_wanted -= 1
    ducks_wanted.pop(0)

    ducks_gave_away += 1


print(ducks_gave_away)
print(total - ducks_gave_away)
