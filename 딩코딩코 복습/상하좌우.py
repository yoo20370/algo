import sys

N = int(sys.stdin.readline().rstrip())
# (행,열)

curr_row = 1
curr_col = 1

command_list = ["L", "R", "U", "D"]
command_num = [(0,-1), (0,1), (-1,0), (1,0)]

for command in sys.stdin.readline().split() :
    # command가 들어오면 command_list를 index로 돌면서 어떤 command인지 체크하고
    # 만약 찾았다면 command_num에 대응되는 값을 start와 end에 더해보고
    # 밖으로 나간다면 아무 것도 하지않고 밖으로 나가지 않는다면 값을 갱신한다.
    # 이것을 모든 커멘드를 처리할 때까지 수행한다. 

    for index in range(len(command_list)) :
        if command == command_list[index] :
            row, col = command_num[index]

            now_row = curr_row + row
            now_col = curr_col + col

            if now_row > 0 and now_row <= N and now_col > 0 and now_col <= N :
                curr_row = now_row
                curr_col = now_col
    
print(curr_row, curr_col)