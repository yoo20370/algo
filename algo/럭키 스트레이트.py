# 캐릭터 점수가 N일 때, N을 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 말한다.

import sys

N = sys.stdin.readline().rstrip()
length = len(N) // 2

a = N[:length]
b = N[length:]

a_sum = 0
b_sum = 0

for index in range(len(a)) :
    a_sum += int(a[index])
    b_sum += int(b[index])

if a_sum == b_sum :
    print("LUCKY")
else :
    print("READY")

