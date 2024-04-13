line = list(input().lower())
wrong = []
for character in line:
    if not character.isalnum() and character != ' ':
        wrong.append(character)
for error in wrong:
    line.remove(error)
answer_list = sorted(list(set(''.join(line).split())))
for answer in answer_list:
    if not answer.isdigit():
        print(answer)


