
def selectSort(arr):

    length = len(arr)

    # i는 정렬될 인덱스 위치 
    for i in range(length-1) :
        minIdx = i
        for j in range(i+1,length) :
            if arr[minIdx] > arr[j] :
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr

arr = [3,2,4,1]

print(selectSort(arr))