### 여기서 핵심은 비교의 경우 방향 그래프 형태로 표현해서 해결할 수 있다는 것 

# 선생님은 시험을 본 학생 N 명의 성적을 분실하고, 성적을 비교한 결과의 일부만 가지고 있다.
# 학생 N 명의 성적은 모두 다르다.

#######################################

# 여기서 4번이 순위가 정확한 이유는 
# 4번 보다 작은 값들은, 모두 4번을 지나거나 도착지이고 
# 4번 보다 큰 값들은 4번이 큰 값들을 지나게 된다. 

# 1번은 5번을 거쳐 4번에 도달 
# 3번과 5번은 4번에 도달 
# 4번은 2번과 6번에 도달 

# 어떻게 구현할까 ?? 
# 모든 노드가 해당 노드를 거쳐가고 해당 노드에서 나가야함 -> 그러면 명확한 순위 결정 가능 
# 1 -> 5,3 -> 4 -> 2, 6

# 제한시간이 5초이고, 주어진 경로 개수가 최대 10,000개 
# 이때 플로이드 워셜을 수행한 뒤 2차원 배열을 순회하면서, 가능한 경우의 수를 기록하면 어떻게 되려나 ??

import sys

INF = int(1e9)

def solution() :

    N, M = map(int, sys.stdin.readline().split())

    graph = [[INF] * N for _ in range(N)]

    for i in range(N) :
        graph[i][i] = 0

    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        graph[start-1][end-1] = 1
    

    for mid in range(N) :
        for start in range(N) :
            for end in range(N) :
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

    result = [0] * N 

    for i in range(N) :
        for j in range(N) :
            if graph[i][j] != 0 and graph[i][j] != INF :
                result[i] += 1
                result[j] += 1

    print(result.count(N-1))

solution()