arr = [30,17,48,5,23,37,50] 

def bst(arr, curr, key) :
    
    if curr >= len(arr) or arr[curr] is None :
        return -1

    if arr[curr] == key :
        return curr
    elif arr[curr] > key :
        return bst(arr, curr * 2 + 1, key)
    elif arr[curr] < key :
        return bst(arr, curr * 2 + 2, key)
    
    return -1
    

print(bst(arr,0 , 70))