
def binary_search(arr, key) -> int:
    pl = 0 
    pr = len(arr) - 1
    
    while pl <= pr :
        mid = (pl + pr) // 2
        if arr[mid] < key :
            pl = mid + 1
        elif arr[mid] > key :
            pr = mid - 1
        else :
            return arr[mid]
    
    return - 1