N, K = map(int, input().split())

dataList = list()
for i in range(1, N+6) :
    if N % i == 0 :
        dataList.append(i)

if K-1 >= len(dataList) :
    print(0)
else :
    print(dataList[K-1]) 