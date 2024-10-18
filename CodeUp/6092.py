N = int(input())
inputList = map(int, input().split())

stuList = [0 for i in range(24)]

for i in inputList :
    stuList[i] += 1

for i in range(1, 24, 1) :
    print(stuList[i], end=" ")
