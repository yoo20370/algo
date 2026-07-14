# 고정점 찾기

# 수열의 원소 중 그 값이 인덱스와 동일한 원소를 의미 
import sys

def solution() :
    
    # 인덱스와 원소의 값이 동일한 값을 찾는 문제
    # 입력값이 매우 크기 때문에 순회 불가
    # 그러므로 이진 탐색을 사용해야 함 
    # 어떤 값을 기준으로 이진탐색을 해야할까 ??
    # 인덱스 ?? 값 ??
    # mid 값이 주어짐 mid 원소가 가리키는 값이 있을 거임 만약 원소의 값이 mid 값보다 작다면 mid 3, 원소 -15 pl = mid + 1 
    # 반대로 원소의 값이 mid 값보다 크다면 mid 3 원소 5 pr = mid - 1
    
    numberCount = int(sys.stdin.readline().rstrip())

    numberList = list(map(int, sys.stdin.readline().split()))

    pl = 0
    pr = numberCount - 1

    while pl <= pr :
        checkIndex = (pl + pr) // 2
        
        # 원소의 값이 checkIndex 값보다 작다면 
        # 오른쪽을 탐색해야 더 큰 원소가 있을 것이고 그래야 checkIndex인 값이 있을 수 있음 
        currentNumber = numberList[checkIndex]
        if currentNumber < checkIndex : 
            pl = checkIndex + 1 

        elif currentNumber > checkIndex :
            pr = checkIndex - 1
        
        else :
            return currentNumber
        
    return -1 

result = solution()
print(result)