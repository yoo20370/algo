N = int(input())



def findNum(n) :
    dataList = list()
    for i in range(2, n + 1 // 2) :
        if n % i == 0 :
            dataList.append(i)
    
    dataList.append(n)
    return dataList

dataList = findNum(N)


def div(N, dataList) : 
    resultList = list()
    while True :
        for i in dataList :
            V = N // i 
            N = V
            R = N % i 

            if V <= i :
                return resultList

            if R == 0 : 
                break
        resultList.append(V)


resultList = div(N, dataList)
print(resultList)


