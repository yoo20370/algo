import sys

N, M = map(int, sys.stdin.readline().split())



coins = list()
for i in range(N) :
    coins.append(int(sys.stdin.readline().rstrip()))

def func(N,M) :
    dp = [10001] * 10001

    