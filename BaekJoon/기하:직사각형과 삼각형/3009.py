def findPoint() :
    pointList = list()

    for i in range(3) :
        x,y = map(int, input().split())
        pointList.append([x,y])

    for i in range(1) :
        for j in range(1,3) :
            x1, y1 = pointList[i]
            x2, y2 = pointList[j]

            print(1, x1, y1, x2 ,y2)
            if x1 != x2 or y1 != y2 :
                print(2, x1, x2, y1, y2)
                return y1, x1
            
print(findPoint())


