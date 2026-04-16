import sys

def solution() :

    N, K = map(int, sys.stdin.readline().split())

    numberList = [i for i in range(1, N + 1)]
    resultList = []

    targetIndex = K - 1
    while numberList :
        resultList.append(numberList.pop(targetIndex))

        targetIndex += K - 1
        while numberList and len(numberList) - 1 < targetIndex :
            targetIndex %= len(numberList)

    print("<" + ", ".join(map(str, resultList)) + ">")

solution()


