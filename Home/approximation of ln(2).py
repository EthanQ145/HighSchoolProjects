a_list = []
for j in range(11):
    a_list.append("")

middle = int(len(a_list)/2)
for k in range(100):
    for i in range(middle):
        a_list = []
        for j in range(11):
            a_list.append("")
        a_list[middle + i] = "|"
        a_list[middle - i] = "|"
        print(' '.join(a_list))
    for i in range(middle):
        a_list = []
        for j in range(11):
            a_list.append("")
        a_list[len(a_list) - i - 1] = "|"
        a_list[i] = "|"
        print(' '.join(a_list))
