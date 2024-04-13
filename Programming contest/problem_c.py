while True:
    given = list(map(int, input().split()))

    if given == [0, 0, 0]:
        break
    else:
        start = given[0]
        step = given[1]
        check = given[2]

        # need to check if it would be bigger or smaller
        if (check > start and step > 0) or (check < start and step < 0):
            if (check - start) % step == 0:
                print(f"Term {int((check - start) / step + 1)}")
            else:
                print("Not in sequence")
        else:
            print("Not in sequence")