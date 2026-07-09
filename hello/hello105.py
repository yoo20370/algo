# 럭키 스트레이트는 특정 조건을 만족해야 발동
# 현재 캐릭터의 점수를 N이라고 할 때
# 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 자릿수의 합을 더한 값이 동일한 상황을 의미 

import sys

def solution(score) :

    scoreNumberList = [int(i) for i in str(score)]

    length = len(scoreNumberList)

    halfIndex = (length // 2)

    leftSum = 0
    rightSum = 0
    for currentIndex in range(length) :
        if currentIndex < halfIndex :
            leftSum += scoreNumberList[currentIndex]
        else :
            rightSum += scoreNumberList[currentIndex]

    if leftSum == rightSum :
        return "LUCKY"
    else :
        return "READY"

score = int(sys.stdin.readline().rstrip())

result = solution(score)
print(result)