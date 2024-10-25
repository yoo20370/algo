N = int(input())

xList = list()
yList = list()
for i in range(N) :
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)
x = max(xList) - min(xList)
y = max(yList) - min(yList)

print(x * y)