
def find(listA) : 
    if listA[0] == listA[1] :
        return listA[2]
    else :
        return listA[0]
listX = list()
listY = list()

for i in range(3) :
    x, y = map(int, input().split())
    listX.append(x)
    listY.append(y)
listX.sort()
listY.sort()

x = find(listX)
y = find(listY)


print(x,y)