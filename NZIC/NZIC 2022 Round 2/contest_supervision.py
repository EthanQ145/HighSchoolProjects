R, C = map(int, input().split())
num_players = int(input())
player_locations = []


for player in range(num_players):
    x, y = map(int, input().split())
    player_locations.append([x, y])
    if x == 0:
        print(y+1)
    else:
        print(y)
