# 접두사 합 사용 
import sys

left, right = map(int, sys.stdin.readline().split())

array = [10, 20, 30, 40, 50]
prefix_sum = [0] * (len(array) + 1)
for i in range(1,len(array) + 1) :
    for j in range(i) :
        prefix_sum[i] += array[j]

print(prefix_sum[right] - prefix_sum[left - 1])