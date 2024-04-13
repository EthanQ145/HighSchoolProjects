A_depends, B_depends, all_ver_A, all_ver_B = map(int, input().split())
A_depends_name = list(input().split())
all_A = []
A_depends_vers = []
for ver in range(all_ver_A):
    A_depends_vers = list(map(int, input().split()))
    all_A.append(A_depends_vers)
B_depends_name = list(input().split())
all_B = []
B_depends_vers = []
for ver in range(all_ver_B):
    B_depends_vers = list(map(int, input().split()))
    all_B.append(B_depends_vers)

common_depends = list(set(A_depends_name).intersection(B_depends_name))

if common_depends:

    def check(a_ver, programs):
        start_count = all_ver_B - 1
        all_check = []
        for B_ver in range(all_ver_B):
            print('start', start_count, 'testing for', programs[0], 'at index', A_depends_name.index(programs[0]), B_depends_name.index(programs[0]))
            print('hello', all_A[a_ver][A_depends_name.index(programs[0])], all_B[start_count][B_depends_name.index(programs[0])])
            if all_A[a_ver][A_depends_name.index(programs[0])] == all_B[start_count][B_depends_name.index(programs[0])]:
                for program in programs[0:]:
                    print('passed')
                    if all_A[a_ver][A_depends_name.index(program)] != all_B[start_count][B_depends_name.index(program)]:
                        all_check.append('wrong')
            else:
                all_check.append('wrong')
            if 'wrong' not in all_check:
                print(start_count)
                return start_count
            else:
                start_count -= 1
                all_check = []
        return "no"


    final_check = False
    count = all_ver_A - 1
    correct = None
    for i in range(all_ver_A):
        print(count, common_depends)
        final_check = check(count, common_depends)
        if final_check != "no":
            correct = count
            break
        else:
            count -= 1

    print(correct, final_check)
else:
    print(all_ver_A - 1, all_ver_B - 1)
