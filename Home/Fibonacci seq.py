start = [0, 1]
count = 0


def fibonacci(N, count):
    if count != 8:
        new_num = N[-1] + N[-2]
        N.append(new_num)
        count += 1
        fibonacci(N, count)
        return N


answer = fibonacci(start, count)
answer.pop(0)
print(answer)
