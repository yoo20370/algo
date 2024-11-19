## 다시 풀어봐야할 것 같다. 차근차근 천천히 풀어보자 

import sys, math

N = int(sys.stdin.readline())

dic = dict()
listA = list()
for i in range(N) :
    data = int(sys.stdin.readline().rstrip())
    listA.append(data)
    
    if dic.get(data) :
        dic[data] = dic.get(data) + 1
    else :
        dic[data] = 1

maxVal = max(dic.values())

# 평균값
avg = int(round(sum(listA) / N, 0))

# 중앙값 
if len(listA) == 1 :
    mid = listA[0]
else :
    listA.sort()
    mid = listA[len(listA) // 2]

# 최빈값 
keys = [k for k, v in dic.items() if v == maxVal]
if len(keys) == 1: 
    minCnt = keys[0]
else :
    keys.sort()
    minCnt = keys[1]

maxVal = max(dic.keys())
minVal = min(dic.keys())

# # 범위값 
# degree = abs(maxVal - minVal)

# print(avg)
# print(mid)
# print(minCnt)
# print(degree)

# #
# import sys
# from collections import Counter

# input = sys.stdin.read
# data = input().split()

# N = int(data[0])
# numbers = list(map(int, data[1:N+1]))

# mean = round(sum(numbers) / N)
# numbers.sort()
# median = numbers[N // 2]

# counter = Counter(numbers)
# modes = [k for k, v in counter.items() if v == max(counter.values())]
# modes.sort()
# mode = modes[0] if len(modes) == 1 else modes[1]

# range_value = max(numbers) - min(numbers)

# print(mean)
# print(median)
# print(mode)
# print(range_value)






