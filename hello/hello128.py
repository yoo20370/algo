# 카드 정렬하기 
# 묶음을 꺼내서 최소 비교를 수행해야 함 
# 즉, 작은 두 개의 값을 비교하는 방향으로 진행하면 될 것 같음 

# 힙 어때 ?? 
# 최소 힙을 통해서 가장 작은 묶음 개수를 가진 두 개의 묶음을 비교해서 다시 넣는 방향으로 

import sys, heapq

def solution() :
    N = int(sys.stdin.readline().rstrip())

    cards = []
    for _ in range(N) :
        card = int(sys.stdin.readline().rstrip())
        heapq.heappush(cards, card)

    
    # 근데 N이 1인 경우는 비교 자체를 안 해도 됨 -> 0 
    # 
    
    totalCompareCount = 0 

    # 결국 2개를 뽑아서 합치고 다시 큐에 넣어야 함 그리고 두 개를 뽑아야 함 
    # 언제까지 반복해야 하는가 ?? cards에 남은 묶음 개수가 1개일 때까지 
    # 결국 cards에 하나의 카드 묶음만 존재할 때까지 진행하면 됨 

    while len(cards) >= 2 :
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)

        compareCount = first + second
        totalCompareCount += compareCount

        heapq.heappush(cards, compareCount)

    return totalCompareCount

result = solution()
print(result)