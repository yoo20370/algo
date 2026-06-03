input = [4, 6, 2, 9, 1]

# 병합 정렬은 원소의 크기가 1이 될 때까지 모두 나눈 뒤, 각각 병합하면서 정렬을 수행하는 정렬 알고리즘 
# 쪼개야 함 

# 쪼갠 다음엔 각 배열의 원소를 비교하면서 하나의 배열로 병합해야 함, 이를 원래의 배열이 될 때 까지 반복 수행한다. 

def merge_sort(array):

    pl = 0 
    pr = len(array) - 1
    mid = (pl + pr) // 2

    if len(array) <= 1 :
        return array
    
    left = merge_sort(array[pl:mid+1])
    right = merge_sort(array[mid+1:])

    result = []

    leftIndex = rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right) : 
        if left[leftIndex] < right[rightIndex] :
            result.append(left[leftIndex])
            leftIndex += 1
        
        else : 
            result.append(right[rightIndex])
            rightIndex += 1
    
    result.extend(left[leftIndex:])
    result.extend(right[rightIndex:])

    return result


merge_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",merge_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",merge_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",merge_sort([100,56,-3,32,44]))