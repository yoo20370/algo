def binary_search(array, key) :
    
    pl = 0
    pr = len(array) - 1

    while pl <= pr :
        mid = (pl + pr) // 2
        if array[mid] < key : 
            pl = mid + 1
        elif array[mid] > key :
            pr = mid - 1
        else : 
            return mid
    
    return -1

