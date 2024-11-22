arr = [1,2,4,5,6,0,0,0,0]
length = 5

def insert(idx, num, arr, len) :
    for i in range(len-1, idx -1, -1) :
        arr[i+1] = arr[i]
    arr[idx] = num
    return len + 1

def erase(idx, arr, len) :
    for i in range(idx, length-1) :
        arr[i] = arr[i+1]
    arr[length-1] = 0
    return len - 1

length = insert(2, 3, arr, length)
print(arr)

length = erase(5,arr,length)
print(arr)
