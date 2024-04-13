def find_multiplier(substance):
    multiplier = []
    valid = True
    for letter in substance:
        if valid:
            if letter.isdigit():
                print(letter)
                multiplier.append(letter)
            else:
                if multiplier:
                    multiplier = int(''.join(multiplier))
                else:
                    multiplier = 1
                valid = False
    return multiplier


print(find_multiplier("42343123H"))

