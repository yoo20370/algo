standard = [1, 1, 2, 2, 2, 8]

listA = list(map(int, input().split()))

for i in range(len(listA)) :
    standard[i] -= listA[i]

for i in standard :
    print(i, end=" ")