text = input().replace(" ", "")
rules = input().split()

if text[int(rules[0])-1] == rules[2] and text[int(rules[1])-1] == rules[3]:
    print("correct")
else:
    print("error")