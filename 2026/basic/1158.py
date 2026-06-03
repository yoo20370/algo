# import sys
# from collections import deque

# def solution(N, K) :

#     result = []
#     remainMember = deque(range(1, N + 1))

#     while remainMember :
#         for _ in range(K - 1) :
#             temp = remainMember.popleft()
#             remainMember.append(temp)
#         result.append(remainMember.popleft())

#     print("<", ", ".join(map(str, result)), ">", sep="")

# N, K = map(int, sys.stdin.readline().split())

# solution(N, K)

## 1, 2, 3, 4, 5, 6, 7

# 0 1 2 3 4 5 6
# 1 4 5 

# current = K - 1
# pop(current)
# 3

# pop(current + K - 1)

# 6

# pop((current + K - 1) % 5)

# 2

# 7

import sys

def solution(N, K) :
    result = []
    members = [i for i in range(1, N + 1)]

    current = K - 1
    while members :
        result.append(members.pop(current))
        if members :
            current = (current + K - 1) % len(members)

    
    print("<", ", ".join(map(str, result)), ">", sep="")

N, K = map(int, sys.stdin.readline().split())

solution(N, K)
