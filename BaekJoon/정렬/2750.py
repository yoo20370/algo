def quickSort(listA) :

    if len(listA) <= 1 :
        return listA

    left = 0
    p = len(listA) // 2 
    right = len(listA) - 1


    leftList = list()
    midList = list()
    rightList = list()

    for i in listA :
        if i < listA[p] :
            leftList.append(i)
        elif i > listA[p] :
            rightList.append(i)
        else :
            midList.append(i)

    return quickSort(leftList) + midList + quickSort(rightList)
N = int(input())

listA = list()
for i in range(N) :
    listA.append(int(input()))
listA = quickSort(listA)

for i in listA :
    print(i)