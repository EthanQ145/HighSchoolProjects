inputted_num = int(input())
count = 0
for i in range(3, inputted_num + 1):
    for j in list(str(i)):
        if j == '3':
            print(i)
            count += 1
print(count)
