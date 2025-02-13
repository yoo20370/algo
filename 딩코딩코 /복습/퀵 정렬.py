input = [4, 6, 2, 9, 1]

def quick_sort(left, right, array):

    pl = left
    pr = right

    p = (pl + pr) // 2
    while pl <= pr :
        while array[pl] < array[p] :
            pl += 1
        while array[p] < array[pr] :
            pr -= 1

        if pl <= pr :
             array[pl], array[pr] = array[pr], array[pl]
             pl += 1
             pr -= 1
    if left <= pr :
        quick_sort(left, pr, array)
    if pl <= right :
        quick_sort(pl, right, array)

    return array

print(quick_sort(0, len(input)- 1, input))
