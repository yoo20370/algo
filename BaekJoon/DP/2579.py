# import sys 

# arr = list()
# N = int(sys.stdin.readline().rstrip())

# arr.append(0)
# for i in range(N) :
#     arr.append(int(sys.stdin.readline().rstrip()))

# def stairUp(arr, idx, cnt) :

#     # 출발점에 도달했거나, 3번 연속 이동하는 경우
#     if idx == 0 or cnt == 3:
#         return 0
    
#     first = 0
#     second = 0

#     if idx - 1 >= 0 :
#         first = stairUp(arr, idx-1, cnt + 1)
#     if idx - 2 >= 0 :
#         second = stairUp(arr, idx-2, 1) 

#     return max(first, second) + arr[idx]  

# print(stairUp(arr, len(arr) - 1, 1))

import sys 

arr = list()
N = int(sys.stdin.readline().rstrip())

arr.append(0)
for i in range(N) :
    arr.append(int(sys.stdin.readline().rstrip()))

dp = [[-1] * 3 for i in range(N+1)]
def stairUp(arr, idx, cnt) :

    # 출발점에 도달했거나, 3번 연속 이동하는 경우
    if idx == 0 or cnt == 3:
        return 0
    
    if dp[idx][cnt] != -1 : 
        return dp[idx][cnt]
    
    first = 0
    second = 0

    if idx - 1 >= 0 :
        first = stairUp(arr, idx-1, cnt + 1)

    if idx - 2 >= 0 :
        second = stairUp(arr, idx-2, 1) 
    dp[idx][cnt] = max(first, second) + arr[idx]  
    return dp[idx][cnt]

print(stairUp(arr, len(arr) - 1, 1))