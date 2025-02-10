input = [4, 6, 2, 9, 1]


def selection_sort(array):
    
    # 삽입할 위치를 도는 반복문이 필요 - n번 모두 돌아야 함 
    # 해당 위치에 들어갈 가장 작은 원소를 찾는다. (오름차순 정렬)
    # i부터 n번 비교하면 된다. -> 가장 작은 값을 가진 인덱스랑, 모든 원소를 비교해야 하기 때문 

    for insert_index in range(len(array) - 1) :
        min_index = insert_index
        for compare_index in range(insert_index + 1, len(array)) :
            if array[min_index] > array[compare_index] :
                min_index = compare_index
        array[insert_index], array[min_index] = array[min_index], array[insert_index]

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))