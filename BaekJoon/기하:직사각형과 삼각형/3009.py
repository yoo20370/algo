def findPoint() :
    pointList = list()

    for i in range(3) :
        x,y = map(int, input().split())
        pointList.append([x,y])

            
print(findPoint())


