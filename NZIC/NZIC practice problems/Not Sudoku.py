board = input().split()
rows = int(board[0])
columns = int(board[1])
possible_numbers = []
not_possible = []
row_index = 0
index = 0
finished_rows = []
for row in range(rows):
    numbers = input().split()
    if "x" in numbers:
        row_index = row
        index = numbers.index("x")
    finished_rows.append(numbers)

for finished_row in finished_rows:
    not_possible.append(finished_row[index])

for number in range(1, rows + 1):
    if str(number) not in not_possible:
        finished_rows[row_index][index] = str(number)

for row in finished_rows:
    print(" ".join(row))


"""
1 2 3 4
2 3 4 5
3 4 5 1 
4 5 1 2 
5 1 x 3

1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 x

1 2 3 4 5 6
2 3 4 5 6 1
3 4 5 6 1 2
4 5 6 1 2 3
5 6 1 2 3 x

"""

