def sortReverse(listA) :
    for i in range(len(listA)) :
        for j in range(i + 1, len(listA)) :
            if listA[i] < listA[j] :
                listA[i], listA[j] = listA[j], listA[i] 
    return listA
N, K = map(int, input().split())
data = list(map(int, input().split()))

data = sortReverse(data)
print(data[K-1])
