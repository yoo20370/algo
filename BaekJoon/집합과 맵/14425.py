# import sys

# def binarySearch(arr, key) :
#     pl = 0
#     pr = len(arr) - 1

#     while pl <= pr :
#         mid = (pl + pr) // 2
#         if arr[mid] < key :
#             pl = mid + 1
#         elif key < arr[mid] :
#             pr = mid - 1
#         else :
#             return 1
#     return 0

# listA = list()
# N, M = map(int, sys.stdin.readline().split())
# for i in range(N) :
#     listA.append(sys.stdin.readline().rstrip())

# listA.sort()

# cnt = 0
# for j in range(M) :
#     data = sys.stdin.readline().rstrip()
#     cnt += binarySearch(listA, data)

# print(cnt)

import sys
N, M = map(int, sys.stdin.readline().split())

setA = set()
for i in range(N) :
    setA.add(sys.stdin.readline().rstrip())

cnt = 0
for i in range(M) :
    data = sys.stdin.readline().rstrip()
    if data in setA :
        cnt += 1

print(cnt)




# 다른 사람의 코드 elroy0920 사람의 코드 
# import sys

# input=sys.stdin.readline
# n,m = map(int, input().split())
# S = set()
# for i in range(n):
#     S.add(input())
# ans = 0
# for _ in range(m):
#     t = input()
#     if t in S:
#         ans += 1
# print(ans)