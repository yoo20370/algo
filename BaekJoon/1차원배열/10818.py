N = int(input())
listA =list(map(int, input().split()))

max = listA[0]
min = listA[0]

for i in range(1,len(listA)) :
    if max < listA[i] :
        max = listA[i]
    if min > listA[i] :
        min = listA[i]
print(min, max)