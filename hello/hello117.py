# 안테나 
# 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치 
# 이때 안테나는 집이 위치한 곳에만 설치 가능 
import sys


def solution() :

    houseCount = int(sys.stdin.readline().rstrip())

    houseList = list(map(int, sys.stdin.readline().split()))

    sortedHouseList = sorted(houseList)

    mid = houseCount // 2

    if houseCount % 2 == 0 :
        mid -= 1

    return sortedHouseList[mid]

result = solution()
print(result)



