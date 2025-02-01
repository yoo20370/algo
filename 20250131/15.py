arr = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8, 8]

MX = max(arr)

listA = [0] * (MX+1)

for i in arr :
    listA[i] += 1


for i in range(MX + 1) :
    for _ in range(listA[i]) :
        print(i, end=" ")


