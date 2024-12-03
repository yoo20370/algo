
# def insertSort(arr) :

#     length = len(arr)

#     for i in range(1, length) :
#         key = arr[i] 
#         idx = i
#         while idx > 0 and arr[idx-1] > key :
#             arr[idx] = arr[idx-1]
#             idx -= 1
#         arr[idx] = key
        

#     return arr

# arr = [3, 2, 4, 1]

# print(insertSort(arr)) 

def insertSort(arr) :

    length = len(arr)

    for i in range(1, length) :
        key = arr[i]
        idx = i 

        while idx > 0 and arr[idx-1] > key :
            arr[idx] = arr[idx-1]
            idx -= 1
        arr[idx] = key
    
    return arr

print(insertSort([3,2,4,1]))