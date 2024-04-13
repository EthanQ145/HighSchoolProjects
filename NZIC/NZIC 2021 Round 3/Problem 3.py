import math
number_wanted = int(input())
cost_two = int(input())
cost_three = int(input())

if cost_two/2 < cost_three/3:
    purchases = number_wanted/2
    if purchases - math.floor(purchases) == 0.5:
        purchases -= 1.5
        extra = 1
    else:
        extra = 0
    lowest_cost = extra * cost_three + purchases * cost_two
    print(int(lowest_cost))
else:
    purchases = number_wanted/3
    if 0.3 < purchases - math.floor(purchases) < 0.4:
        purchases = math.floor(purchases) - 1
        extra = 2
    elif 0.6 < purchases - math.floor(purchases) < 0.7:
        purchases = math.floor(purchases)
        extra = 1
    else:
        extra = 0
    lowest_cost = extra * cost_two + purchases * cost_three
    print(int(lowest_cost))

