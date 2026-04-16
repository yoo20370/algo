# 병합 정렬 -> 배열 길이가 1이 될 때까지 쪼개라 
# 배열 길이가 1이면 이제 거꾸로 왼쪽 배열과 오른쪽 배열의 원소를 비교하여 하나의 배열로 만든다.


def merge_sort(array):
    
    if len(array) <= 1 :
        return array
    
    pl = 0
    pr = len(array) - 1
    mid = (pl + pr) // 2

    left = merge_sort(array[:mid + 1])
    right = merge_sort(array[mid + 1 :])

    result = list()
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right) :

        if left[left_index] < right[right_index] :
            result.append(left[left_index])
            left_index += 1

        else :
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ", merge_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", merge_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",merge_sort([100,56,-3,32,44]))