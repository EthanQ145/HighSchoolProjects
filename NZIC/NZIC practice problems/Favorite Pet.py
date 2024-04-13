scores = input().split()
highest_score = 0
for score in scores:
    if highest_score < int(score):
        highest_score = int(score)
print("Pet", scores.index(str(highest_score)) + 1)
