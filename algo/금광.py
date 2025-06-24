# 첫 번째 열부터 금을 캐기 시작, 몇 번째 행이든 출발 가능 
# m번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동,
# 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램 

# 딱 떠오른 생각은 완전 탐색을 수행해야한다는 것 
# 동일한 2차원 배열을 만들어 두고 각 위치에 대한 최대값을 구하여 저장하도록 하는 것 
# 즉 1열을 기준으로 2열의 최대값을 구해서 저장하고, 2열을 기준으로 최대값 구하기 .... 
# 마지막 열 중 최대값을 뽑아내면 될 것 같음 

import sys 

def gold_mine() :
    row, col = map(int, sys.stdin.readline().split())

    data = list(map(int, sys.stdin.readline().split()))

    graph = [[0] * col for _ in range(row)]
    for index in range(len(data)) :
        r = index // col
        c = index % col 

        graph[r][c] = data[index]
    
    # memo 테이블에는 항상 그 위치의 최대값이 들어가야 함 
    memo = [[0] * col for _ in range(row)]

    for curr_row in range(row) :
        memo[curr_row][0] = graph[curr_row][0]
    
    # 오른쪽 위, 오른쪽, 오른쪽 아래 
    move_list = [(-1, 1), (0, 1), (1, 1)]

    answer = 0 
    # 어떻게 ?? 
    # 특정 열의 로우를 순회하면서, 해당 r,c에서 이동 가능한 위치 값을 구한다. 그리고 max(a, b)를 구해서 해당 위치에 저장한다. 
    for curr_col in range(col) :
        for curr_row in range(row) :

            for next_row, next_col in move_list :
                move_row = curr_row + next_row
                move_col = curr_col + next_col  

                if move_row >= 0 and move_row < row and move_col >= 0 and move_col < col :
                    # 최대값은 이전에 계산한 최대값 혹은 이전 열의 최대값 + 원래 금광의 금액 
                    memo[move_row][move_col] = max(memo[move_row][move_col], memo[curr_row][curr_col] + graph[move_row][move_col])

                    answer = max(answer, memo[move_row][move_col])
    
    return answer

def solution() :
    try_count = int(sys.stdin.readline().rstrip())

    for _ in range(try_count) :
        print(gold_mine())


solution()