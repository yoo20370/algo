# 1차 시도 
# import sys

# def binarySearch(arr, key) :
#     pl = 0 
#     pr = len(arr) - 1

#     while pl <= pr :
#         mid = (pl + pr) // 2
#         if arr[mid] > key :
#             pl = mid + 1
#         elif arr[mid] < key :
#             pr = mid - 1
#         else :
#             return mid

#     return -1  

# N, M = map(int, sys.stdin.readline().split())

# riceCakes = list(map(int, sys.stdin.readline().split()))

# riceCakes.sort(reverse=True)

# setA = set()

# maxHeight = 0
# for height in range(riceCakes[0]-1, -1, -1) :
#     result = binarySearch(riceCakes, height+1) 

#     if result != -1 :
#         setA.add(riceCakes[result])
        
#     sumVal = 0
#     for riceCake in setA :
#         sumVal += riceCake - height
    
#     # print(setA, height, sumVal)
#     if sumVal == M :
#         maxHeight = height
#         break

# print(maxHeight)
    

import sys

N, M = map(int, sys.stdin.readline().split())

riceCakes = list(map(int, sys.stdin.readline().split()))

maxHeight = max(riceCakes)

def findMaxHeight(maxHeight) :
    pl = 0
    pr = maxHeight
    maxVal = 0 
    while pl <= pr :
        mid = (pl+pr) // 2

        result = sum(max(0, height - mid) for height in riceCakes)

        # 제일 높은 값을 출력해야 하는데 그렇지 않음 
        if result >= M : 
            maxVal = max(maxVal, mid)
            pl = mid + 1
        elif result < M :
            pr = mid - 1
    
    return maxVal

print(findMaxHeight(maxHeight))
