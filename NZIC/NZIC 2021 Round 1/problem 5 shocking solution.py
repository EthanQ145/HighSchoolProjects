LIST_OF_NUM = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
LIST_OF_SYMBOLS = ['+', '*']
wanted_result = int(input())
shock_number = input().split()
shock_symbol = input().split()
print(shock_number)
should_use_number = []
smallest_num = shock_number[0]
while shock_number:
    shock_number_archive = shock_number
    for i in range(1, len(shock_number)):
        if shock_number[i] < smallest_num:
            smallest_num = shock_number[i]
    should_use_number.append(LIST_OF_NUM[shock_number_archive.index(smallest_num)])
    print(shock_number)
    shock_number.remove(smallest_num)
    if shock_number:
        smallest_num = shock_number[0]
print(should_use_number)


   ### symbol_use = min(shock_symbol)
    ###should_use_symbol = LIST_OF_SYMBOLS.index(symbol_use)