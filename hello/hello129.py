# 공유기 설치

# 틀림
# 이진 탐색은 단조성을 찾아라....
# 풀다가 너무 복잡해진다 싶으면 잘못된 것인지 한 번 생각해볼 것 
import sys

def solution() :


    houseCount, routerCount = map(int, sys.stdin.readline().split())
    
    houseLocations = []

    for _ in range(houseCount) :
        houseLocation = int(sys.stdin.readline().rstrip())
        houseLocations.append(houseLocation)

    sortedHouseLoactions = sorted(houseLocations)

    pl = 1 
    pr = sortedHouseLoactions[-1] - sortedHouseLoactions[0]

    result = 0

    while pl <= pr :

        mid = (pl + pr) // 2

        count = 1
        last = sortedHouseLoactions[0]

        for i in range(1, houseCount) :
            if sortedHouseLoactions[i] - last >= mid :
                count += 1
                last = sortedHouseLoactions[i]

        if count >= routerCount :
            result = mid 
            pl = mid + 1
        else :
            pr = mid - 1

    return result
        

result = solution()
print(result)