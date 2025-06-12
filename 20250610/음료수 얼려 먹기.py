import sys

# dfs를 이용해서 푼다. 
# 2차원 배열을 하나하나 순회하면서, 값이 0이면 count 값을 올리고 dfs로 가능한 탐색 영역을 모두 탐색한다. 이 때 0을 1로 바꾸는 것을 방문처리로 본다.

def dfs(row, col, start_row, start_col, graph) :
    distance = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    stack = [(start_row, start_col)]

    while stack :
        curr_row, curr_col = stack.pop()
        graph[curr_row][curr_col] = 1   # 방문처리 
    
        for next_row, next_col in distance :
            move_row = curr_row + next_row 
            move_col = curr_col + next_col

            if move_row >= 0 and move_row < row and move_col >= 0 and move_col < col and graph[move_row][move_col] == 0 :
                stack.append((move_row, move_col))
    

row, col = map(int, sys.stdin.readline().split())

total_count = 0
graph = []
for _ in range(row) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

for r in range(row) :
    for c in range(col) :
        if graph[r][c] == 0 :
            dfs(row, col, r, c, graph)
            total_count += 1

print(total_count)