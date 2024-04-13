revenue = 0

bid_price = []
for customer in range(int(input())):
    bid_price.append(int(input()))

phone_price = []
for phone in range(int(input())):
    price = int(input())
    if price in bid_price:
        revenue += price
        bid_price.remove(price)
        if not bid_price:
            break
    elif price < max(bid_price):
        phone_price.append(price)

while phone_price and bid_price:
    if max(phone_price) < max(bid_price):
        revenue += max(phone_price)
        bid_price.remove(max(bid_price))
    phone_price.remove(max(phone_price))

print(revenue)
