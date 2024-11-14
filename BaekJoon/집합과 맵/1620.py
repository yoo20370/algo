import sys

N, M = map(int, input().split())

listA = [[] for _ in range(1000)]
listB = [[] for _ in range(1000)]

for i in range(1, N+1) :
    data = sys.stdin.readline().rstrip()

    hashVal = int(i) % 1000
    hashVal2 = hash(data) % 1000

    listA[hashVal].append([i, data])
    listB[hashVal2].append([i, data])


result = list()
def func(hashTable, data, n) :
    # 숫자인 경우
    if n == 0 :
        hashVal = int(data) % 1000
        for i in hashTable[hashVal] :
            if int(i[0]) == int(data) :
                result.append(i[1])
    else :
        hashVal = hash(data) % 1000
        for i in hashTable[hashVal] :
            if i[1] == data :
                result.append(i[0])

for i in range(M) :
    data = sys.stdin.readline().rstrip()
    if data.isdigit() :
        func(listA, data, 0)
    else :
        func(listB, data, 1)

for i in result :
    print(i)

