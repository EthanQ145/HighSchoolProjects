x_place = 0
y_place = 0
shortest_distance = 0
count = 0
num_cars = int(input())
for car in range(num_cars):
    shortest_distance = x_place ** 2 + y_place ** 2
    if x_place == y_place:
        x_place += 1
        y_place = 0
    elif x_place > y_place:
        if count == 0:
            count += 1
            pass
        elif count == 1:
            y_place += 1
            count = 0
print(shortest_distance)

"""num_cars = int(input())
count = 0
shortest_distance = 0
while int(num_cars**0.5 + 0.5)**2 != num_cars:
    num_cars += 1
    count += 1
shortest_distance = int(((num_cars**0.5) - count/2))^2 + \
                    int(((num_cars**0.5) - (count+ 0.5)/2))^2
print(shortest_distance)"""


