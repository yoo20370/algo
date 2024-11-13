def quick(arr, left, right, option) :

    pl = left 
    pr = right
    p = arr[(left + right) // 2][option]

    while pl <= pr :
        while arr[pl][option] < p :
            pl += 1
        while p < arr[pr][option] :
            pr -= 1

        if pl <= pr :
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    
    if left < pr :
        quick(arr, left, pr, option)
    if pl < right :
        quick(arr, pl, right, option)

N = int(input())

arr = list()
for i in range(N) :
    x, y = map(int, input().split())
    arr.append([x,y])

quick(arr, 0, len(arr)-1, 1) 

s = 0
for i in range(1, N + 1) :
    if i == N or arr[i][1] != arr[s][1] :
        quick(arr, s, i-1, 0) 
        s = i

for x, y in arr :
    print(x, y)
