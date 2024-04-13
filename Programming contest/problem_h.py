num_sets = int(input())
for i in range(num_sets):
    card_1, card_2, card_3 = input().split()
    property_dict = {"Colour": [card_1[0], card_2[0], card_3[0]],
                     "Number": [card_1[1], card_2[1], card_3[1]],
                     "Shape": [card_1[2], card_2[2], card_3[2]],
                     "Fill": [card_1[3], card_2[3], card_3[3]]}
    set = True
    for value in property_dict.values():
        for val in value:
            if value.count(val) == 2:
                set = False

    if set:
        print("Set")
    else:
        print("Not a Set")