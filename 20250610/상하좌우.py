import sys

N = int(sys.stdin.readline().rstrip())

curr_row = curr_col = 1

command_dic = {
    'L' : (0, -1),
    'R' : (0, 1),
    'U' : (-1, 0),
    'D' : (1, 0)
}

for command in sys.stdin.readline().split() :
    move_row, move_col = command_dic.get(command)

    next_row = curr_row + move_row
    next_col = curr_col + move_col

    if next_row > 0 and next_row < N + 1 and next_col > 0 and next_col < N + 1 :
       curr_row = next_row
       curr_col = next_col 

print(curr_row, curr_col)
