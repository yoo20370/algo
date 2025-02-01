
# def binary_search(arr, key) :

#     pl = 0 
#     pr = len(arr) -1

#     while pl <= pr :
#         mid = (pl + pr) // 2

#         if arr[mid] < key :
#             pl = mid + 1
#         elif arr[mid] > key :
#             pr = mid - 1
#         else :
#             return mid
    
#     return -1

def binary_search(arr, pl, pr, key) :

    if pl > pr :
        return -1

    mid = (pl+pr) // 2
    if arr[mid] < key :
        return binary_search(arr, mid + 1, pr, key)
    elif arr[mid] > key :
        return binary_search(arr, pl, mid - 1, key)
    else :
        return mid 