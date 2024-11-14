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




