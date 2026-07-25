import sys 
from collections import deque

def check_line(row, col, N) :
    if row >= 0 and row < N and col >= 0 and col < N :
        return True
    return False

def check_visited(row, col, visited) :
    if (row, col) not in visited :
        return True
    return False

def check_condition(value1, value2, L, R) :

    result = abs(value1 - value2)
    if L <= result and result <= R :
        return True
    return False

def solution() :
    N, L, R = map(int, sys.stdin.readline().split())

    graph = []

    direction = [(1,0), (-1,0), (0,1), (0,-1)]

    for _ in range(N) :
        graph.append(list(map(int, sys.stdin.readline().split())))

    turn = 0
    while True :
        union_count = 0

        visited = set()

        queue = deque()

        union_group = []
        
        for r in range(N) :
            for c in range(N) : 
                if check_line(r, c, N) and check_visited(r, c, visited) :
                    queue.append((r, c, turn))
                    visited.add((r,c))

                    union = []
                    while queue :
                        curr_row, curr_col, curr_turn = queue.popleft()
                        union.append((curr_row, curr_col))

                        for move_row, move_col in direction :

                            next_row = curr_row + move_row
                            next_col = curr_col + move_col
                            
                            if check_line(next_row, next_col, N) and check_visited(next_row, next_col, visited) and check_condition(graph[curr_row][curr_col], graph[next_row][next_col], L, R) :
                                visited.add((next_row,next_col))
                                queue.append((next_row, next_col, curr_turn))
                            
                    # 이게 1이라는 소리는 무슨 소리일까 ?? -> 인접한 도시 중에 연합한 녀석이 없다는 의미 
                    if len(union) <= 1 :
                        continue
                    
                    union_group.append(union)

        for union in union_group :
            # 인구 이동
            result = 0 
            for curr_row, curr_col in union :
                result += graph[curr_row][curr_col]

                # 인구 이동 결과 저장 
            result = result // len(union) 
            for curr_row, curr_col in union :
                graph[curr_row][curr_col] = result

        # 첫 번째 턴에, 연합 자체가 없다면, 인구 이동이 없는 것 -> 
        if turn == 0 and len(union_group) == 0 :
            return 0
        elif turn != 0 and len(union_group) == 0 :
            return turn

        turn += 1 

print(solution())
