# 병사 배치하기
# N명의 병사 무작위로 나열 
# 각 병사는 전투력 보유 
# 병사 배치 시 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 함
# 배치 과정에서 특정한 위치에 있는 병사를 열외시키는 방법 이용 
import sys 

def solution() :
    length = int(sys.stdin.readline().rstrip())

    soldierList = list(map(int, sys.stdin.readline().split()))

    dp = [1] * length 

    for currentIndex in range(1, length) :

        currentAttackStat = soldierList[currentIndex]
        for preIndex in range(0, currentIndex) :

            preAttackStat = soldierList[preIndex]

            if currentAttackStat < preAttackStat :
                dp[currentIndex] = max(dp[currentIndex], dp[preIndex] + 1)


    return length - max(dp)



result = solution()

print(result)