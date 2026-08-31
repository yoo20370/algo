# 못 생긴 수 
# 못 생긴 수란 2, 3, 5만을 소인수로 가지는 수를 의미 
# 2, 3, 5를 약수로 가지는 합성수를 의미한다. 
# n 번째 못생긴 수를 찾는다 
# 1은 못생긴 수라고 가정 

# 10 -> 12
# 4 -> 4


import sys

MAX = int(101)

dp = [False] * MAX

dp[1] = dp[2] = dp[3] = dp[5] = True

def checkUglyNumber(number) :
    
    if number == 0 :
        return False

    if dp[number] == True :
        return True

    if number % 2 == 0 :
        dp[number] = checkUglyNumber(number // 2) 
    elif number % 3 == 0 :
        dp[number] = checkUglyNumber(number // 3)
    elif number % 5 == 0 :
        dp[number] = checkUglyNumber(number // 5)

    return dp[number]

def solution() :
    # 2, 3, 5로 먼저 나누고 다른 수로 나누어 떨어지는지 확인해야 함 
    # 이때 앞에서 이미 못 생긴 수라는 판단을 먼저 하면서 이후 나누어 떨어진 수가 못생긴 수인지 체크해야 겠음 

    targetNumber = int(sys.stdin.readline().rstrip())

    for number in range(4, MAX) :
        checkUglyNumber(number)


    currentSequence = 0
    for number in range(1, MAX) :
        if dp[number] == True :
            currentSequence += 1

        if currentSequence == targetNumber :
            print(number)
            break


    
    

solution()