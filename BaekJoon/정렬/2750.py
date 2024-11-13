def quick(arr, left, right) :

    pl = left
    pr = right
    p = arr[(left + right) // 2]

    while pl <= pr :
        while arr[pl] < p :
            pl += 1
        while p < arr[pr] :
            pr -= 1
        
        if pl <= pr :
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    
    if left < pr :
        quick(arr, left, pr) 
    if pl < right :
        quick(arr, pl, right)

N = int(input())

data = list()
for i in range(N) :
    data.append(int(input()))

quick(data, 0, len(data) - 1)

for i in data :
    print(i)