players = list(range(1, int(input()) + 1))

for total_info in range(int(input())):
    info = input().split()
    if info[0] == 't':
        if int(info[1]) in players:
            players.remove(int(info[1]))
        else:
            players.append(int(info[1]))
            players = sorted(players)
    elif info[0] == 'o':
        if int(info[1]) in players:
            print(players.index(int(info[1])) + 1)
        else:
            print('UNOFFICIAL')


