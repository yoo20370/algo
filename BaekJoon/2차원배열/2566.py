N = M = 9


max = 0
row = 0
column = 0
for i in range(N) :
    listA = list(map(int, input().split())) 
    for j in range(M) :
        if max < listA[j] :
            max = listA[j]
            row = i
            column = j 
    
print(max)
print(row+1, column+1)