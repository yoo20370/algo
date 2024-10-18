N = int(input())
stuList = list(map(int, input().split()))

min = 10000
for i in stuList :
    if min > i :
        min = i
print(min)