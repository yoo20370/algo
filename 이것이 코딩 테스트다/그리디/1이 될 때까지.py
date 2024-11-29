# import sys

# N, K = map(int, sys.stdin.readline().split())

# remain = N 
# cnt = 0
# while remain % K != 0 :
#     remain -= 1
#     cnt += 1

# while remain // K != 0 :
#     remain = remain // K
#     cnt += 1

# while remain != 1 :
#     remain -= 1
#     cnt += 1

# print(cnt)

import sys

N, K = map(int, sys.stdin.readline().split())

def check(N, K) :

    

    remain = 0
    cnt = 0
    while N // K != 0 :
        remain += N % K 
        N = N // K
        cnt += 1

    while N != 1 :
        N -= 1
        cnt += 1

    print(remain + cnt)

check(N, K)