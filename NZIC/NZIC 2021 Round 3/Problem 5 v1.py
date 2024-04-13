players = int(input())

unofficial_players = []
for total_info in range(int(input())):
    info = input().split()
    if info[0] == 't':
        if info[1] in unofficial_players:
            unofficial_players.remove(info[1])
        else:
            unofficial_players.append(info[1])
    elif info[0] == 'o':
        if info[1] in unofficial_players or int(info[1]) > players:
            print('UNOFFICIAL')
        else:
            answer = int(info[1])
            for unofficial_player in unofficial_players:
                if int(info[1]) > int(unofficial_player):
                    answer -= 1
            print(answer)



