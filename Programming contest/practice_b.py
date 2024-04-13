actual_dict = {}
town_list = []
num = 1

while True:
    input_thingy = input()

    try:
        int(input_thingy)
        if town_list:
            actual_dict[num] = len(town_list)
            num += 1
            town_list = []
        if input_thingy == "0":
            break
    except ValueError:
        if input_thingy not in town_list:
            town_list.append(input_thingy)


for thing in actual_dict:
    print(f"Week {thing} {actual_dict[thing]}")
