array = [5, 3, 2, 1, 6, 8, 7, 4]

def merge_sort(array):
    # 배열의 모든 원소가 1개가 될 때까지 나눈다.
    if len(array) <= 1 :
        return array
    
    mid = len(array) // 2

    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    result = merge(left_array, right_array)

    return result

def merge(array1, array2):

    resultList = []

    left_index = 0
    right_index = 0 

    while left_index < len(array1) and right_index < len(array2) :
        if array1[left_index] <= array2[right_index] :
            resultList.append(array1[left_index])
            left_index += 1
        else :
            resultList.append(array2[right_index])
            right_index += 1

    while left_index < len(array1) :
        resultList.append(array1[left_index])
        left_index += 1
    while right_index < len(array2) :
        resultList.append(array2[right_index])
        right_index += 1

    return resultList

print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))