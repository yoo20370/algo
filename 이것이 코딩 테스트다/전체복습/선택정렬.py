arr = [1,3,2,6,5,4,9,8,0]

def selectSort(arr) -> None :
    for i in range(len(arr)-1) :
        min_idx = i
        for j in range(i + 1, len(arr)) :
            if arr[min_idx] > arr[j] :
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


selectSort(arr)

print(arr)
