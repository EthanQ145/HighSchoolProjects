number_of_sums = int(input())
for total in range(number_of_sums):
    number_of_lines = int(input())
    pound = 0
    shillings = 0
    pence = 0
    for line in range(number_of_lines):
        money = input().split('-')
        pounds = list(money[0])
        pounds.remove('#')
        money[0] = ''.join(pounds)
        pound += int(money[0])
        shillings += int(money[1])
        pence += int(money[2])

    while pence >= 12:
        pence -= 12
        shillings += 1

    while shillings >= 20:
        shillings -= 20
        pound += 1

    print('#' + str(pound) + '-' + str(shillings) + '-' + str(pence))


