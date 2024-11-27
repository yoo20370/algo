import sys

N = int(sys.stdin.readline().rstrip())


dp = [0] * (N+1)

def easyStair(n) :
    if n == 1 :
        return 9

    return  easyStair(n-1) * 2 - n + 1

print(easyStair(N) % 1000000000)