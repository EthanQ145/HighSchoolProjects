lines = []
ships = []
for i in range(0, 10):
    line = input()
    lines.append(line.split())
    for location in line.split():
        if location != "#":
            ships.append(location)
attack = [1, 2]
while [attack[0], attack[1]] != ["-1", "-1"]:
    attack = input().split()
    if lines[int(attack[1])][int(attack[0])] != "#" and \
            [attack[0], attack[1]] != ["-1", "-1"]:
        if ships.count(lines[int(attack[1])][int(attack[0])]) > 1:
            print(f"Hit {lines[int(attack[1])][int(attack[0])]}")
        else:
            print(f"Sunk {lines[int(attack[1])][int(attack[0])]}")
        ships.remove(lines[int(attack[1])][int(attack[0])])
        lines[int(attack[1])][int(attack[0])] = "#"
    elif [attack[0], attack[1]] != ["-1", "-1"]:
        print("Miss")
