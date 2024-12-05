# 이진탐색으로 풀기
# import sys 

# def binarySearch(arr, key) :
#     pl = 0
#     pr = len(arr) - 1

#     while pl <= pr :
#         mid = (pl + pr) // 2
#         if arr[mid] < key :
#             pl = mid + 1
#         elif arr[mid] > key :
#             pr = mid - 1
#         else :
#             return mid
    
#     return -1

# N = int(sys.stdin.readline().rstrip())

# parts = list(map(int, sys.stdin.readline().split()))
# parts.sort()
# M = int(sys.stdin.readline().rstrip())

# for i in map(int, sys.stdin.readline().split()) :
#     if binarySearch(parts, i) == -1 :
#         print("no", end=" ")
#     else :
#         print("yes", end=" ")

# 계수 정렬 풀이 
import sys 
N = int(sys.stdin.readline().rstrip())

MX = 1000001
parts = [0] * MX 

for i in map(int, sys.stdin.readline().split()) :
    parts[i] += 1

M = int(sys.stdin.readline().rstrip()) 

for i in map(int, sys.stdin.readline().split()) :
    if parts[i] == 0 :
        print("no", end = " ")
    else :
        print("yes", end =" ")