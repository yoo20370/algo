## 어떻게 풀어야 할까나 ?? 

# 자주 나오는 값은 어떻게 풀어야 할까 ?? 
# 순회하면서 몇 개 나왔는지 카운트하고 기록하는 것 
# 그리고 한 번 더 돌면서 최대값이 무엇인지 확인하기 
# 한 번 더 돌면서 크기의 값이 있는지 확인하기 

## 각 숫자는 몇 번 등장했지 ?? 

## 가장 자주 나온 값이 뭐지 ?? 

## 가장 자주 나온 값은 유일 값인가 ?? 

import sys
MX = 1001

def solution(array) :
    countList = [0] * MX 

    # 각 숫자는 몇 번 등장했는가 
    for currentNumber in array :
        countList[currentNumber] += 1

    # 가장 자주 나온 값의 횟수는 ?? 
    maxNumberCount = max(countList)

    maxIndex = 0
    count = 0
    for currentNumber in countList :
        if countList[currentNumber] == maxNumberCount :
            maxIndex = currentNumber
            count += 1

    
    if count == 1 :
        print(maxIndex)
    
    elif count > 1 :
        print(-1)    


# map 
array = list(map(int, sys.stdin.readline().split()))

solution(array)


