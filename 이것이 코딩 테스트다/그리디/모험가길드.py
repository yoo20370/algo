import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

avg = sum(arr) // N

cnt = 0
for item in arr :
    if  item >= avg :
        cnt += 1
     
result = cnt // avg
print(result)

