# 요세푸세 

# 큐를 이용해서 푸는 것이 가장 쉽습니다.

# 큐 풀이 방법 

import sys
from collections import deque

# 이 방식은 n과 k가 크면 시간복잡도가 매우 큼 
# 그 계속해서 큐를 수정해줘야 하기 때문 
def solution_queue() :

    n, k = map(int, sys.stdin.readline().split())

    people = deque([i for i in range(1, n + 1)])

    result = []

    while people :

        for _ in range(k-1) :
            temp = people.popleft()
            people.append(temp)
        
        result.append(people.popleft())
    

    print(result)

solution_queue()


def solution() :

    n, k = map(int, sys.stdin.readline().split())

    people = [i for i in range(1, n + 1)]

    result = []

    targetIndex = k - 1
    while people :
        target = people.pop(targetIndex)
        result.append(target)

        # 왜 k-1을 이동하나요 ?? -> 리스트에서 제거되기 때문에 한 칸 이동한 것이나 마찬가지이기 때문 
        targetIndex += k - 1
        while people and targetIndex >= len(people) :
            targetIndex %= len(people)

    print(result)
solution()
