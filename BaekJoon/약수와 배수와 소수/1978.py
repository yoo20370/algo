N = int(input())

listA = list(map(int, input().split()))


def findNum(n) :
    if n == 1 :
        return 0
    if n == 2 :
        return 1
    
    for i in range(2,n+1 // 2) :
        if n % i == 0 :
            return 0

    return 1 

cnt = 0
for i in  listA :
    cnt += findNum(i)

print(cnt)