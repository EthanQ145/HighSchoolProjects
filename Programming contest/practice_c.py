counts = int(input())
answer_list = []

for times in range(counts):
    ranges = list(map(int, input().split()))
    S = ranges[0]
    F = ranges[1]
    C = ranges[2]
    answer = 0
    for i in range(S, F+1):
        if str(C) in list(str(i)):
            answer += 1
    answer_list.append(answer)

for answer in answer_list:
    print(answer)
