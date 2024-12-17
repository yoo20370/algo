# import sys

# N, K = map(int, sys.stdin.readline().split())

# cnt = 0 
# while N != 1 :

#     if N % K == 0 :
#         N = N // K 
#     else : 
#         N -= 1
#     cnt += 1

# print(cnt)

import sys

N, K = map(int, sys.stdin.readline().split())

result = 0
while True :
    target = (N // K) * K
    result += (N - target)
    N = target

    if N < K :
        break

    result += 1
    N //= K

result += (N-1)
print(result)