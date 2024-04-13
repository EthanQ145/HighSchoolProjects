import math

age = int(input())
min_age = int(input())

real_age = math.floor(age/2)
if real_age < min_age:
    print('No')
else:
    print('Yes')
