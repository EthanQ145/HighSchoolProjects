A_depends, B_depends, all_ver_A, all_ver_B = map(int, input().split())
A_depends_name = list(input().split())
all_A = []
for ver in range(all_ver_A):
    all_A.append(list(map(int, input().split())))
B_depends_name = list(input().split())
all_B = []
for ver in range(all_ver_B):
    all_B.append(list(map(int, input().split())))

common_depends = list(set(A_depends_name) & set(B_depends_name))

if common_depends:

    def check(a_ver, programs):
        start_count = all_ver_B - 1
        a_thing = all_A[a_ver]
        a_first = A_depends_name.index(programs[0])
        b_first = B_depends_name.index(programs[0])
        for B_ver in range(all_ver_B):
            b_thing = all_B[start_count]
            if a_thing[a_first] == b_thing[b_first]:
                if check_2(a_thing, b_thing, programs[1:]):
                    print(a_ver, start_count)
                    return None
            start_count -= 1
        return False

    def check_2(check_a, check_b, things_to_check):
        for thing in things_to_check:
            if check_a[A_depends_name.index(thing)] != check_b[B_depends_name.index(thing)]:
                return False
        return True


    final_check = False
    count = all_ver_A - 1
    for i in range(all_ver_A):
        final_check = check(count, common_depends)
        if final_check is not False:
            break
        else:
            count -= 1

else:
    print(all_ver_A - 1, all_ver_B - 1)
