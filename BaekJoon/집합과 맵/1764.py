import sys

def binarySearch(arr, key) :
    pl = 0
    pr = len(arr) - 1

    while pl <= pr :
        mid = (pl + pr) // 2
        if arr[mid] < key :
            pl = mid + 1
        elif key < arr[mid] :
            pr = mid - 1
        else :
            return arr[mid]
    return -1

N, M = map(int, input().split())

listA = list()
for i in range(N) :
    listA.append(sys.stdin.readline().rstrip())

listA.sort()

resultList = list()
for i in range(M) :
    data = sys.stdin.readline().rstrip()
    
    result = binarySearch(listA, data)
    if result != -1 :
        resultList.append(result)

# resultList.append(str(len(resultList)))
resultList.sort()


for i in resultList :
    print(i)

# set 연산자 
# import sys
# N, M = map(int, sys.stdin.readline().split())

# A = set()
# B = set()
# for _ in range(N):
#     A.add(input())
# for _ in range(M):
#     B.add(input())

# len_result = A&B
# result = list(len_result)
# result.sort()
# print(len(len_result))
# for i in range(len(len_result)):
#     print(result[i])

