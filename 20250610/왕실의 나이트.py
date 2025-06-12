import sys 

N = 8

input_data = sys.stdin.readline().rstrip()

curr_row = ord(input_data[0]) - ord('a') + 1
curr_col = int(input_data[1])

move_list = [(2,1), (2,-1), (-2,1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

move_count = 0
for move_row, move_col in move_list :

    next_row = curr_row + move_row
    next_col = curr_col + move_col

    if next_row > 0 and next_row < N + 1 and next_col > 0 and next_col < N + 1 :
        move_count += 1

print(move_count)
