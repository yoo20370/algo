def sort(listA) :

    for i in range(len(listA)) :
        for j in range(len(listA)) :
            if listA[i] > listA[j] :
                listA[i], listA[j] = listA[j], listA[i] 
    
    return listA

data = list()
sum = 0
for i in range(5) :
    a = int(input())
    data.append(a)
    sum += a

data = sort(data)
print(sum // 5)
print(data[len(data) // 2])


