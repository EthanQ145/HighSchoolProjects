total_lines = int(input())
all_columns = []
all_rows = []
total_column = 0
total_row = 0
total_moves = 0
for line in range(total_lines):
    position = input().split()
    column = int(position[0])
    row = int(position[1])
    all_columns.append(column)
    all_rows.append(row)
    total_column += column
    total_row += row

average_column = total_column/len(all_columns)
average_row = total_row/len(all_rows)

if abs(average_column - max(all_columns)) > abs(average_row - max(all_rows)):
    chosen_position = average_row
    for move in all_rows:
        total_moves += abs(move - chosen_position)
else:
    chosen_position = average_column
    for move in all_columns:
        total_moves += abs(move - chosen_position)

print(int(total_moves))
