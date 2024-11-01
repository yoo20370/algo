# N, R = map(int, input().split())

# listA = list(map(int, input().split()))

# max = 0 
# for i in range(N-2) :
#     for j in range(i+1, N-1) :
#         for z in range(j + 1, N) :
#             result = listA[i] + listA[j] + listA[z] 
#             if max < result and result <= R :
#                 max = result

# print(max)        

from itertools import combinations
N, R = map(int, input().split())
dataList = list(map(int, input().split()))

max = 0
for data in combinations(dataList, 3) :
    sumVal = sum(data)
    if sumVal > max and sumVal <= R :
        max = sumVal

print(max)