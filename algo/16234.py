# 각 땅에는 나라가 하나씩 존재 
# r행 c연에 있는 나라에는 A[r][c]명이 살고 있다. 
# 인접한 나라 사이에는 국경선이 존재 
### 하루 동안 다음과 같이 진행, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 반복 
## 국경선을 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하라면 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
## 위의 조건에 의해 열어야 하는 국경선이 모두 열렸다면, 인구 이동을 시작한다. 
## 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다. 
## 연합을 이루고 있는 각 칸의 인구수는(연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
## 연합을 해체하고 모든 국경선은 닫는다. 
### 처음부터 연합이 하나도 없다면, 0을 반환해야 함 -> 

### 어떻게 풀어야 하나 ? 
### 연합을 구성해야겠다. -> 연합 구성 후, 계산을 수행하여 인구 이동 시작하고 결과를 저장 
### 여러 연합이 있을 수 있으므로 이를 반복한다.
### 연합이 한 개가 되면 끝나는 것 

### 모든 r, c에 대해서 순회하면서, 연합으로 참여하지 않았다면 그 도시에 대하여 bfs를 수행한다.
### 왜냐하면 이미 연합에 참여했다는 것은 bfs에 참여했다는 것이므로 하루에는 더 이상 할 필요가 없어짐 
### turn을 가져야 할 듯, -> 몇 번째에 끝나는지 확인해야 하므로 
### 만약, turn이 1인데, 연합이 전혀 없다면 -> 0을 반환
### turn이 1이 아닌데 연합이 전혀 없는 경우 -> turn 반환 

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
