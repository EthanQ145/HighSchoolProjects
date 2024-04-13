length_of_code = int(input())
code = list(input())
translation_possible = 0

vowels = ['a', 'e', 'i', 'o', 'u']
index = 0
vowel = 0
consonant = 0

if code[-1] != 'k':
    # Type is Goose with lf last
    for letters in code:
        if letters in vowels:
            vowel += 1
        translation_possible = int(vowel/2)
    print(translation_possible)

elif code[-1] == 'k':
    if code[-2] != 'c':
        # Type is honk
        for letter in code:
            if letter in vowels:
                vowel += 1
        if vowel - 1 == 0 and len(code) > 3:
            translation_possible += 1
        print(translation_possible)
    else:
        if code[-3] != 'a':
            pass
else:
    print(translation_possible)


