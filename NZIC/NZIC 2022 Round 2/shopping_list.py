food_items = int(input())
money_spent = 0
for num in range(food_items):
    how_much = list(map(int, input().split()))
    wanted = how_much[0]
    price_1 = how_much[2]
    price_2 = how_much[4]
    stock_1 = how_much[1]
    stock_2 = how_much[3]
    amount_bought = 0

    if price_1 < price_2:
        if stock_1 <= wanted:
            money_spent += stock_1 * price_1
            amount_bought = stock_1
            while amount_bought < wanted:
                amount_bought += 1
                money_spent += price_2
        else:
            money_spent += wanted * price_1
    else:
        if stock_2 <= wanted:
            money_spent += stock_2 * price_2
            amount_bought = stock_2
            while amount_bought < wanted:
                amount_bought += 1
                money_spent += price_1
        else:
            money_spent += wanted * price_2

print(money_spent)

