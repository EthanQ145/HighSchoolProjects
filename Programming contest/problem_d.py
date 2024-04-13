car_park = input().split()
available = int(car_park[0])
current = int(car_park[1])
entries = list(input())
valid = True
for entry in entries:
    if entry == "O":
        if current != 0:
            current -= 1
        else:
            valid = False
            break
    if entry == "I":
        if current < available:
            current += 1
if valid:
    print(f"{current} cars.")
else:
    print('Error.')
