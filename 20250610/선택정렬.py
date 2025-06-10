input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 선택 정렬이란 순회하며 정렬할 데이터를 선택하는 정렬 알고리즘이다. (최대값, 최소값을 선택하고 확정) O(N**2) 시간 복잡도를 갖는다. 
    # 재자리 정렬, 불안정 정렬(동일한 값이 순서대로 들어오더라도, 다른 순서로 정렬될 수 있음)
    # 바깥쪽 반복문은 저장할 위치 
    # 안쪽 반복문은 매번 배열을 순회하며 최소값을 찾는다.

    for i in range(len(array) - 1) :
        min_index = i
        for j in range(i + 1, len(array)) :
            if array[min_index] > array[j] :
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))