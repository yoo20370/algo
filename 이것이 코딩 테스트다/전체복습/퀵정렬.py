arr = [1,3,2,6,5,4,9,8,0]

def quick_sort(arr, left, right) -> None :

    pl = left 
    pr = right 
    pivot = arr[(pl + pr) // 2]

    while pl <= pr :
        while arr[pl] < pivot :
            pl += 1
        while arr[pr] > pivot :
            pr -= 1
        
        if pl <= pr :
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    
    if pl < right :
        quick_sort(arr, pl, right) 
    if left < pr :
        quick_sort(arr, left, pr)

quick_sort(arr, 0, len(arr)-1)

print(arr)