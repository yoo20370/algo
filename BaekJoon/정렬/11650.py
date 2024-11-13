
def sort(arr, s, e, o) :    
    for i in range(s, e-1) :
        for j in range(i+1, e) :
            if arr[i][o] > arr[j][o] :
                arr[i], arr[j] = arr[j], arr[i]

def quick(arr, left, right, o) :

    pl = left
    pr = right
    p = arr[(pl + pr) // 2][o]

    while pl <= pr :
        while arr[pl][o] < p :
            pl += 1
        while p < arr[pr][o] :
            pr -= 1

        if pl <= pr :
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    if left < pr :
        quick(arr, left, pr, o)
    if right > pl :
        quick(arr, pl, right, o)

N = int(input())

arr = list()
for i in range(N) :
    x, y = map(int, input().split())
    arr.append([x,y])

quick(arr, 0, len(arr)-1, 0)

s = 0 
for i in range(1, N+1) :
    if i == N or arr[s][0] != arr[i][0] :
        quick(arr, s, i-1, 1) 
        s = i

for x, y in arr :
    print(x,y)
