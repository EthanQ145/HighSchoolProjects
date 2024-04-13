N, A, B = map(int, input().split())
temps = list(map(int, input().split()))
first_good = 0
good = 0
stack = 0
stack_ends = 0
stack_list = []

for i in range(len(temps)):
    if i >= stack_ends:
        if A <= temps[i] <= B:
            print("RAN AT INDEX", i, temps[i])
            good += 1
            first_good = i
            stack += 1
        if good != 0:
            after_index = temps[first_good + 1:]
            print(after_index)
            for j in range(len(after_index)):
                if A > after_index[j] or B < after_index[j]:
                    print('the number is bad', after_index[j])
                    good -= 1
                    if good == 0 and j + 2 <= len(after_index) and (A > after_index[j + 1] or after_index[j + 1] > B):
                        (print('trip stops'))
                        break
                    else:
                        stack += 1
                else:
                    good += 1
                    stack += 1
                    print('the number is good', after_index[j], 'good is', good)
                print('stack is', stack)
                stack_ends = j + 1
        if good > 0 and first_good != 0:
            print('yes')
            if good - 1 <= len(temps[:first_good]):
                stack += good - 1
            else:
                stack += len(temps[:first_good])
        if stack > 0:
            stack_list.append(stack)
            stack = 0
            good = 0

print(stack_list)
if stack_list:
    print(max(stack_list))
else:
    print(0)



