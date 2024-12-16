import sys 

INF = int(1e9)

cityCnt = int(sys.stdin.readline().rstrip())
busCnt = int(sys.stdin.readline().rstrip())

# 모두 INF로 초기화 
route = [[INF] * (cityCnt+1) for _ in range(cityCnt + 1)]

# 자기 자신으로 가는 경우 0으로 초기화
# for i in range(1, cityCnt+1) :
#     route[i][i] = 0

for i in range(1, cityCnt + 1) :
    for j in range(1, cityCnt + 1) :
        if i == j :
            route[i][j] = 0

for _ in range(busCnt) :
    cityA, cityB, cost = map(int, sys.stdin.readline().split())
    route[cityA][cityB] = min(route[cityA][cityB], cost)

def floyd() :
    for mid in range(1, cityCnt+1) :
        for start in range(1, cityCnt+1) :
            for end in range(1, cityCnt+1) :
                route[start][end] = min(route[start][end], route[start][mid] + route[mid][end])

floyd()

for cityA in range(1, cityCnt+1) :
    for cityB in range(1, cityCnt+1) :
        if route[cityA][cityB] == INF :
            print(0,end=" ")
        else :
            print(route[cityA][cityB], end=" ")
    print()
