listA = [False for _ in range(42)]

for i in range(10) :
    N = int(input())

    reval = N % 42
    listA[reval] = True

cnt = 0 
for i in listA :
    if i == True :
        cnt += 1
print(cnt)