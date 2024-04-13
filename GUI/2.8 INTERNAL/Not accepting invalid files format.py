try:
    ENGLISH_WORDS_LEVEL_1 = open("English words 1").readlines()
except UnicodeDecodeError:
    ENGLISH_WORDS_LEVEL_1 = ''
if ENGLISH_WORDS_LEVEL_1 == '':
    print('Invalid file format, make sure it is a text file!')
else:
    for word in ENGLISH_WORDS_LEVEL_1:
        print(word)
