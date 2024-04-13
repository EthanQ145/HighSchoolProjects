import math

small = int(input())
medium = int(input())
large = int(input())
row_1 = []
row_2 = []
row_3 = []

largest_num = small
if medium > largest_num:
    largest_num = medium
if large > largest_num:
    largest_num = large

difference_small = int(math.floor(largest_num - small)/2)
difference_medium = int(math.floor(largest_num - medium)/2)
difference_large = int(math.floor(largest_num - large)/2)

leftover_small = (largest_num - small) - difference_small

leftover_medium = (largest_num - medium) - difference_medium

leftover_large = (largest_num - large) - difference_large

print('_'*difference_large + 'L'*large + '_'*leftover_large)
print('_'*difference_medium + 'M'*medium + '_'*leftover_medium)
print('_'*difference_small + 'S'*small + '_'*leftover_small)
