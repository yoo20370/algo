import sys

def quick(arr, left, right) -> None :
    pl = left
    pr = right 
    p = arr[(pl+pr) // 2]

    while pl <= pr :
        while arr[pl] > p :
            pl += 1
        while arr[pr] < p :
            pr -= 1

        if pl <= pr :
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1

    if left < pr :
        quick(arr,left, pr)
    if pl < right :
        quick(arr, pl, right) 


N = int(sys.stdin.readline().rstrip())

arr = list()
for _ in range(N) :
    arr.append(int(sys.stdin.readline().rstrip()))

quick(arr, 0, len(arr)-1)

for num in arr :
    print(num)