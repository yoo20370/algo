def binarySearch(arr, key) :
    pl = 0
    pr = len(arr) - 1
    
    while pl <= pr :
        mid = (pl + pr) // 2
        if arr[mid] < key :
            pl = mid  + 1
        elif key < arr[mid] :
            pr = mid - 1
        else :
            return arr[mid]
    return -1 