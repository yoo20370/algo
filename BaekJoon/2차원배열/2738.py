N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]

for i in range(2) :
    for j in range(N) :
        listA = list(map(int, input().split()))
        for z in range(M) :
            arr[j][z] += listA[z]

for i in range(N) :
    for j in range(M) :
        print(arr[i][j], end=" ")
    print()