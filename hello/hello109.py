# N개의 원소를 포함하고 있는 수열이 오름 차순으로 정렬되어 있다. 
# 이때 이 수열에서 x가 등작하는 횟수를 구하여라 

# 순회는 O(N) 이므로 불가능 -> 데이터가 너무 많기 때문
# 이진 탐색을 수행해서 가장 왼쪽의 인덱스와 가장 오른쪽의 인덱스를 구해야할 것 같음 

# 가장 먼저 떠오른 건 이진탐색 두 번 수행하는 거 

import sys

INF = int(1e9)

def solution() :

    length, target = map(int, sys.stdin.readline().split())

    sortedArray = list(map(int, sys.stdin.readline().split()))

    pl = 0
    pr = length - 1 

    maxIndex = -1
    minIndex = INF 
    # 최대 위치를 구해야 함 
    while pl <= pr :
        mid = (pl + pr) // 2

        if sortedArray[mid] <= target :
            if sortedArray[mid] == target :
                maxIndex = max(maxIndex, mid)

            pl = mid + 1
        else  :
            pr = mid - 1  

    pl = 0
    pr = length - 1 
    minIndex = INF 
    while pl <= pr :
        mid = (pl + pr) // 2

        if sortedArray[mid] >= target :
            if sortedArray[mid] == target :
                minIndex = min(minIndex, mid)

            pr = mid - 1
        else  :  
            pl = mid + 1

    if maxIndex == -1 or minIndex == INF :
        return -1 
    
    return maxIndex - minIndex + 1 
    
result = solution()
print(result)


