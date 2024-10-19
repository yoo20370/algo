cnt, val = map(int, input().split())
listA = list(map(int, input().split()))

for i in listA :
    if i < val :
        print(i, end=" ")        