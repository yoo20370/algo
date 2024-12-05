# 값을 찾는 재귀함수 이진탐색 
# def binarySearch(arr, key) :
#     if len(arr) == 1 and arr[0] != key :
#         return -1 
    
#     start = 0
#     end = len(arr) - 1 
#     mid = (start + end) // 2

#     result = -1
#     if arr[mid] > key :
#         result = binarySearch(arr[:mid],key)
#     elif arr[mid] < key :
#         result = binarySearch(arr[mid+1:],key) 
#     else :
#         return arr[mid]

#     return result

# 인덱스를 찾는 재귀함수 이진탐색 
# def binarySearch(arr, start, end, key) :
#     if start > end :
#         return -1 
    
#     mid = (start + end) // 2
#     result = -1 
#     if arr[mid] > key :
#         result = binarySearch(arr, start, mid-1, key)
#     elif arr[mid] < key :
#         result = binarySearch(arr, mid + 1, end, key)
#     else :
#         return mid
    
#     return result


def binarySearch(arr, key) :
    pl = 0 
    pr = len(arr) - 1

    while pl <= pr :
        mid = (pl + pr) // 2
        if arr[mid] < key :
            pl = mid + 1
        elif arr[mid] > key :
            pr = mid - 1
        else :
            return mid

    return -1  


arr = [0,2,4,6,8,10,12,16,18]

print(binarySearch(arr, 4))