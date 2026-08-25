# 볼링공 고르기
# 서로 무게가 다른 볼링공을 고르려고 한다.
# 볼링공은 총 N개가 있음 
# 각 볼링공마다 무게가 적혀 있음 

# 같은 무게의 공이 있을 수 있지만, 서로 다른 공으로 간주 
# 서로 무게가 다른 것으로 고르곘다. 
# 어려운 문제가 아닌 듯 곱셈으로 해결할 수 있을 듯

# 1 2 2 3 3 
# 1 * 4 + 2 * 2



# 1 2 2 3 4 4 5 5
# 1 * 7 + 2 * 5 + 1 * 4 + 2 * 2

# # 정의해보면 
# # 현재 고른 무게 개수 * 나머지 개수 (단, 작은 값은 제외 이미 처리되었기 때문)

# # 이제 방법은 알았는데 어떻게 코드를 짜야할까 
# # 한 번 순회해서 개수를 배열에 저장해두고 

# # 누적시켜가면서 전체 개수에서 뺀 값을 가지고 다루는거지 
import sys 

def solution() :
    count, maxWeight = map(int, sys.stdin.readline().split())

    ballList = list(map(int, sys.stdin.readline().split()))

    ballCountList = [0 for _ in range(maxWeight + 1)]

    for weight in ballList :
        ballCountList[weight] += 1 

    totalCount = 0 
    usedCount = 0
    for weight in range(1, maxWeight + 1) :
        currentWeightCount = ballCountList[weight]
        usedCount += currentWeightCount
        totalCount += currentWeightCount * (count - usedCount)

    print(totalCount)

solution()





