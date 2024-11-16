M = int(input())
N = int(input())


def findNum(n) :

    if n == 1 :
        return 0
    elif n == 2 :
        return 1
    
    for i in range(2, n + 1 // 2) :
        if n % i == 0 :
            return 0
    
    return 1


listA = list()
for i in range(M, N+1) :
    if 1 == findNum(i) :
        listA.append(i)

if len(listA) != 0 :
    print(sum(listA))
    print(min(listA))
else :
    print(-1)
