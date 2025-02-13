input = [4, 6, 2, 9, 1]


def merge(left_array, right_array) -> list:
    result_list = []

    left_index = 0
    right_index = 0

    while left_index < len(left_array) and right_index < len(right_array) :
        if left_array[left_index] < right_array[right_index] :
            result_list.append(left_array[left_index])
            left_index += 1
        else : 
            result_list.append(right_array[right_index])
            right_index += 1
    
    while left_index < len(left_array) :
        result_list.append(left_array[left_index])
        left_index += 1

    while right_index < len(right_array) :
        result_list.append(right_array[right_index])
        right_index += 1
 
    return result_list

def merge_sort(array):

    if len(array) == 1 :
        return array
    
    pl = 0 
    pr = len(array) - 1
    mid = (pl + pr) // 2

    return merge(merge_sort(array[:mid+1]), merge_sort(array[mid+1:]))


merge_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",merge_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",merge_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",merge_sort([100,56,-3,32,44]))