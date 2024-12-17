# import sys
# arrSize, addCnt, limit = map(int, sys.stdin.readline().split())

# arr = list(map(int, sys.stdin.readline().split()))

# arr.sort(reverse=True)

# sumVal = 0
# for order in range(1, addCnt+1) :
#     if order % (limit+1) == 0:
#         sumVal += arr[1]
#     else :
#         sumVal += arr[0]

# print(sumVal)

import sys
arrSize, addCnt, limit = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse=True)

cycle = addCnt // (limit + 1)
remain = addCnt % (limit + 1)

bigNum = cycle * arr[0] * limit
bigNum += remain * arr[0]
smallNum = cycle * arr[1]

print(bigNum +smallNum)