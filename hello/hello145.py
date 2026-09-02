# 행성 터널 

# 왕국은 N개의 행성으로 이루어져 있다. 
# 행성을 연결하는 터널을 만드려고 한다.
# 행성은 3차원 좌표 위의 한 점으로 생각하면 됨 

# 터널 N - 1개를 건설해서, 모든 행성이 서로 연결되게 만들어야 한다. 
# 이때 모든 행성을 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성해라 

# 이거는 최소 신장 트리 문제임 
# 결국 비용을 구해서 힙에 저장하거나 그냥 비용을 기준으로 정렬을 한 뒤 비용이 적은 간선부터 연결하면 될 것 같다.

# 근데 문제는 결국 입력값임.... 10만이라 n * n - 1 -> O(N**2)이라 어려움
# 즉, 모든 거리를 계산하지 말고 필요한 거리만 계산하는 방법이 필요함 

# 갑자기 떠오른 생각은 각 행성과 가까운 행성이 있을 거임 그걸 바탕으로 해야 하나 ? 
# 이것도 결국 모든 거리가 동일하고 멀게 되면 의미가 없어짐, 즉 확정적이지 않음...

# 프림 알고리즘을 써야 하나 ? 
# ㄴㄴ 의마가 없는게 비용을 구하는게 시간복잡도가 큰 거임 
# 사실 찾는 메커니즘 자체 크게 차이가 안 남

# 비용을 구하는 걸 어떻게 시간복잡도를 줄일 수 있을까 ?? 
# 다 구할 필요가 있는가 ? -> X 
# 가장 가깝고 아직 연결안 된 행성을 연결하면 되는 거 아닌가 ? 

# 현재 행성에서 가장 가까운 행성 연결 
# 다음 행성도 가장 가까운 행성과 연결
# 그러면 가장 가까운 행성이라는 걸 어떻게 구할 거임 ?? 
# 1. 두 점 사이의 거리를 구하고 비교하는 것 -> 검사 비용 막대함 
# 2. 정렬하면 뭔가 가능할 것 같은데

# 방법이 도저히 떠오르지 않아 답 확인
# 1. 가장 가까운 행성 후보를 추려낸다. - 각 축을 기준으로 양 옆을 확인하면 됨 (최대 6개) - 가장 가까운 행성을 찾는 것은 특정 축이며, 그 축에서 가장 가까이 앞 혹은 뒤에 있는 두 점 중 하나가 가장 가까운 게 됨 
# 2. 이들을 리스트에 넣고 비용을 기준으로 정렬한다. - 6개의 후보중 가장 가까운 값을 구해야 함 
# 3. 크루스칼 알고리즘을 이용해서 푼다. 


import sys 

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y) :

    parentX = find(parent, x)
    parentY = find(parent, y)

    if parentX < parentY :
        parent[parentY] = parentX
    else :
        parent[parentX] = parentY

def solution() :

    planetCount = int(sys.stdin.readline().rstrip())

    xList = []
    yList = []
    zList = []

    for currentPlanet in range(planetCount) :
        x, y, z = map(int, sys.stdin.readline().split())

        xList.append([x, currentPlanet])
        yList.append([y, currentPlanet])
        zList.append([z, currentPlanet])


    sortedX = sorted(xList)
    sortedY = sorted(yList)
    sortedZ = sorted(zList)

    edgeList = []
    for currentIndex in range(planetCount - 1) :

        planetA = sortedX[currentIndex + 1][1]
        planetB = sortedX[currentIndex][1]
        cost = min(abs(xList[planetA][0] - xList[planetB][0]), abs(yList[planetA][0] - yList[planetB][0]), abs(zList[planetA][0] - zList[planetB][0]))
        edgeList.append((cost, planetA, planetB))

    

        planetA = sortedY[currentIndex + 1][1]
        planetB = sortedY[currentIndex][1]
        cost = min(abs(xList[planetA][0] - xList[planetB][0]), abs(yList[planetA][0] - yList[planetB][0]), abs(zList[planetA][0] - zList[planetB][0]))
        edgeList.append((cost, planetA, planetB))

        planetA = sortedZ[currentIndex + 1][1]
        planetB = sortedZ[currentIndex][1]
        cost = min(abs(xList[planetA][0] - xList[planetB][0]), abs(yList[planetA][0] - yList[planetB][0]), abs(zList[planetA][0] - zList[planetB][0]))
        edgeList.append((cost, planetA, planetB))


    edgeList.sort()

    parent = [i for i in range(planetCount)]

    totalCost = 0
    for currentEdge in edgeList :
        cost, planetA, planetB = currentEdge

        if find(parent, planetA) != find(parent, planetB) :
            union(parent, planetA, planetB)
            totalCost += cost

    return totalCost

result = solution()
print(result)