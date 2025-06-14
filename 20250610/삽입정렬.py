input = [4, 6, 2, 9, 1]

def insertion_sort(array):
    # 삽입 정렬이란, 삽입할 위치를 찾는 정렬 알고리즘으로 O(N**2) 시간 복잡도를 갖는다. 단, 앞이 정렬되어있다고 가정하기 때문에 이미 정렬되어 있는 경우 O(N) 시간 복잡도를 갖는다.
    # 재자리 정렬, 안정 정렬 
    # 어떻게 구현 ??
    # 첫 번째 반복문의 인덱스는 1부터 ~ len(array) 순회 -> 원소를 선택 
    # 두 번째 반복문의 경우 앞으로 이동하며, 원소가 삽입될 위치를 찾아주는 역할 

    for i in range(1, len(array)) :
        j = i
        temp = array[i]

        # 조건을 만족하면 뒤로 이동시킴
        while j - 1 >= 0 and array[j - 1] > temp :
            array[j] = array[j - 1]
            j -= 1

        # 더 이상 이동할 수 없을 때, 해당 공간에 삽입 
        array[j] = temp 

    return array

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))