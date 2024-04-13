shoes = list(input())
count = 0
for shoe in shoes:
    if shoe == 'R':
        count += 1
if count == 0:
    print('Maybe Dorothy is in Kansas.')
elif count == 1:
    print('Hop along Dorothy and find that other shoe.')
else:
    print('Dorothy is in the classroom.')