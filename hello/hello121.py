# 탑승구

# G개의 탑승구가 있다. 
# 공항에는 P개의 비행기가 차례대로 도착할 예정

# i번째 비행기를 1번부터 gi번째 탑승구 중 하나에 영구적으로 도킹해야 함 
# 이때 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있다. 
# 또한 P개의 비행기를 순서대로 도킹하다가 만약에 어떤 탑승구에도 도킹할 수 없는 비행기가 오는 경우, 그 시점에는 공항의 운행을 중지 
###  공항 관리자는 최대한 많은 비행기를 공항에 도킹하고자 한다.
### 비행기를 최대한 몇 대까지 도킹할 수 있는지를 출력하는 프로그램을 작성하라 

## 문제 이해부터 해야할 듯 
# 도킹 조건 ? 

# 4 - 탑승구 수
# 3 - 비행기 수 
# 4, 1, 1

# 최대 2대 가능 

# 탑승구 1 2 3 4 
# 비행기 4 1 1 

# 내가 이해한 건 다음과 같음 
# 결국, 순서대로 처리할 거고 비행기의 번호가 있는데 이 번호가 탑승구의 번호보다 크거나 같은 경우
# 즉, 탑승구 번호가 더 큰 경우 배치 불가 

# 결국 큰 숫자가 들어오면 어디에든 들어갈 수 있음 
# 반면 작은 숫자 일수록 도킹 가능한 게이트가 적어짐 

# 결국 간단하게 생각하면 입력으로 들어온 값에 해당하는 게이트를 사용해버리도록 함 
# 입력으로 들어온 값의 게이트가 이미 존재한다면 이보다 작은 게이트를 앞으로 탐색하는 경우로 처리해야 함 (순회)
# 결국 O(N**2)이 됨 -> 불가능

# 유니온 파인드를 사용하면 될 것 같음 
# 일단 비행기의 경우 본인의 번호로 등록하고자 시도함 
# 만약 현재 게이트 번호가 사용 중이라면 (parent x와 number가 서로 다른 값인 경우) 
# 결국 find(parent, x)를 진행했을 때 반환되는 부모의 값이 현재 비행기가 들어갈 게이트가 됨 
# 만약 0이 반환된다면 -> 들어갈 최대 위치가 없다는 뜻이므로 종료시켜야 함 

import sys

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]
 
def solution() :
    gateCount = int(sys.stdin.readline().rstrip())
    planeCount = int(sys.stdin.readline().rstrip())

    gateStatusList = [i for i in range(gateCount + 1)]

    dockingCount= 0 
    for _ in range(planeCount) :
        currentPlaneNumber = int(sys.stdin.readline().rstrip())

        dockingGateNumber = find(gateStatusList, currentPlaneNumber)

        if dockingGateNumber == 0 :
            return dockingCount
        
        dockingCount += 1

        gateStatusList[dockingGateNumber] = find(gateStatusList, dockingGateNumber - 1)

result = solution()
print(result)