N = int(input())
stuList = list(map(int, input().split()))

for i in range(len(stuList)-1, -1, -1) :
    print(stuList[i], end=" ")