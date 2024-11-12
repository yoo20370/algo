# 병합 정렬 
# 재귀 함수 

N = int(input())

data = list()
for i in range(N) :
    data.append(int(input()))

def mergeSort(arr) :
    length = len(arr) 

    if length == 1 :
        return arr 

    pl = 0
    pr = length - 1
    mid = length // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    result = list()
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right) :
        if left[left_idx] < right[right_idx] :
            result.append(left[left_idx])
            left_idx += 1
        else :
            result.append(right[right_idx])
            right_idx += 1
    
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

data = mergeSort(data)

for i in data :
    print(i)