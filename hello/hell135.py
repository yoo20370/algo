# 만들 수 없는 금액 
# 틀림

# N개의 동전을 가지고 있음 
# 만들 수 없는 금액 중 최소값을 8원 

# 백트래킹 -> 시간초과 

# 정렬 후, 최소값을 증명해내가는 방법을 사용함
# 앞에서부터 값을 합하는 경우, 합해진 값까지는 모두 만들 수 있음 


import sys

def solution() :

    coinCount = int(sys.stdin.readline().rstrip())
    coins = list(map(int, sys.stdin.readline().split()))

    totalSum = sum(coins)

    sortedCoins = sorted(coins)

    avaliableNumber = 0

    currentIndex = 0 
    targetNumber = 1
    for currentNumber in sortedCoins :
        if targetNumber < currentNumber :
            return targetNumber
        targetNumber += currentNumber


result = solution()
print(result)

