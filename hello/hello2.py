# 배열에 있는 수를 N번 더하여, 가장 큰 수를 만드는 법칙
# 연속해서 K번을 초과해서 같은 수가 나오면 안 된다. 

# K - 1번 가장 큰 횟수가 나오고, 1번 두 번째로 큰 수를 계산한다. 그리고 이걸 몇 번 나올 수 있는지 확인한다.
# 나머지는 가장 큰 수라고 판단하여 더해준다.

import sys

N, M, K = map(int, sys.stdin.readline().split())

numberList = list(map(int, sys.stdin.readline().split()))

numberList.sort(reverse=True)

totalSum = 0

firstNumber = numberList[0]
secondNumber = numberList[1]

cycleMaxSum = firstNumber * (K - 1) + secondNumber
maxSumCount = N // K 

totalSum = maxSumCount * cycleMaxSum
remainCount = N % K

totalSum += totalSum + (firstNumber * remainCount)

print(totalSum)

