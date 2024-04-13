N = input()
for i in range(1, int(N) + 1):
    if i%3 == 0 and i%5 == 0:
        i = "FizzBuzz"
    else:
        if i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"
    print(i)
