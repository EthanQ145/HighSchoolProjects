moves = input().split()

position = int(moves[0])

# mark as visited
visited = [int(moves[0])]

# check if house is ever smaller than 1 or bigger than 20
# check if house has already been visited too

legal = True

for move in moves[1:]:
    # move to a place
    if move[0] == "U":
        position += int(move[1])
    else:
        position -= int(move[1])
    # check if visited and if in range
    if position in visited or position > 20 or position < 1:
        legal = False
    visited.append(position)

if legal:
    if len(visited) == 20:
        print("none")
    else:
        # find not visited
        not_visited = []
        for i in range(1, 21):
            if i not in visited:
                not_visited.append(i)
        print(" ".join(map(str, not_visited)))
else:
    print("illegal")