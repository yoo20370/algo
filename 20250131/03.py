import sys

N, K = map(int, sys.stdin.readline().split())


cnt = 0 
while N >= K :

    remain = N % K
    N -= remain
    cnt += remain

    N //= K 
    cnt += 1

cnt += (N - 1)

print(cnt)
    


    




