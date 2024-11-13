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
inputData = list(map(int, input().split()))

arr = list()
for i in range(len(inputData)) :
    # 값, 변경값, 인덱스 
    arr.append([inputData[i], 0, i])

quick(arr, 0, len(arr)-1, 0)

s = 1
arr[0][1] = 0 
for i in range(1, len(arr)) :
    if arr[i-1][0] == arr[i][0] :
        arr[i][1] = arr[i-1][1]
    else :
        arr[i][1] = s
        s += 1

quick(arr, 0, len(arr)-1, 2)

for x, y, z in arr :
    print(y, end=" ")