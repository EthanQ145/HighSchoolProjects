student_dict = {}
night_info = {}
night_count = 1
while True:
    given_input = input()
    try:
        room_number, name = given_input.split()
        student_dict[room_number] = name
    except:
        odd_even, multiple, first_letter = given_input.split()
        night_info[night_count] = [odd_even, multiple, first_letter]
        night_count += 1
        if night_count > 5:
            break

noisy_students = []
for night, info in night_info.items():
    for num, name in student_dict.items():
        if ((info[0] == "O" and int(num) % 2 == 0) or
            (info[0] == "E" and int(num) % 2 != 0)) and \
                int(num) % int(info[1]) != 0 and name[0] != info[2]:
            noisy_students.append(name)

max_num = 0
for student in noisy_students:
    max_num = max(noisy_students.count(student), max_num)

final_students = []
for student in noisy_students:
    if noisy_students.count(student) == max_num and student not in final_students:
        final_students.append(student)

final_nums = []
for student in final_students:
    for num, name in student_dict.items():
        if name == student:
            final_nums.append(num)

for num in sorted(final_nums):
    print(student_dict[num])