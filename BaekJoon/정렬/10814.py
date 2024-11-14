def quick(arr, left, right, option) :
    pl = left
    pr = right
    p = arr[(pl + pr) // 2][option]

    while pl <= pr :
        while arr[pl][option] < p :
            pl += 1
        while p <  arr[pr][option] :
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
    x, y = input().split()
    arr.append([int(x), y, i])

quick(arr, 0, len(arr)-1, 0)

s = 0
for i in range(1, N + 1) :
    if i == N or arr[s][0] != arr[i][0] :
        quick(arr, s, i - 1, 2)
        s = i

for x, y, z in arr :
    print(x, y)



