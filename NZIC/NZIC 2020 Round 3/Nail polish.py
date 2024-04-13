first = list(input())
all_colours = []
bad_ = False


if len(first) == len(set(first)):
    for i in range(4):
        colours = list(input())
        if all_colours:
            if len(colours) >= len(all_colours[-1]):
                bad_ = True
                print("bad")
                break
        all_colours.append(colours)
    if not bad_:
        print("ok")
else:
    for i in range(4):
        colours = list(input())
        if len(colours) % 2 == 0:
            bad_ = True
            print("bad")
            break
    if not bad_:
        print("best")


