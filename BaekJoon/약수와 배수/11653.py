def findNum(n) :
    dataList = list()
    for i in range(2, n + 1 // 2) :
        if n % i == 0 :
            dataList.append(i)
    
    dataList.append(n)
    return dataList

def div(N, dataList) :
    if len(dataList) <= 1 :
        return ""
    
    minNum = min(dataList)
    
    while True :
        beforeNum = 0
        for i in dataList :
            remain = N % i
            valNum = N / i
            beforeNum = i
            if valNum != float(int(valNum)) :
                continue
            else : 
                N = remain
                print(int(i))
                break
        if N <= beforeNum :
            break


N = int(input())
# 약수 구하기
dataList = findNum(N)
div(N,dataList)
