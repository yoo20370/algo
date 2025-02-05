import sys

N = int(sys.stdin.readline().rstrip())

# 경우의 수 
cnt = 0

a = 1 
# N - (a + a + 2) 값
while N - (a + a + 2) >= 0 :
    # 남은 사탕 모두 c에게 준다. 
    c = N - (a + a + 2) 

    # 짝수면 카운트
    if c != 0 and c % 2 == 0 :
        cnt += 1

    a += 1


print(cnt)
