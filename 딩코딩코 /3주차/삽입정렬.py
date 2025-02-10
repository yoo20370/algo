input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    
    # 삽입할 위치를 선정하는 정렬 알고리즘 
    # 삽입할 위치 다음 원소에서 시작하여 앞으로 이동하며 삽입할 위치를 찾는 정렬 알고리즘 
    # 이 때, 앞에 원소들은 이미 정렬되어 있다고 가정한다. 

    # 첫 번째 반복분은 1부터 배열의 길이까지 반복한다. 원소를 선택을 반복문
    # 두 번째 반복문은 첫 번째 반복문의 변수부터 0까지 반복하며, 삽입할 위치를 찾아야 한다. 

    for curr_index in range(1, len(array)) :
        insert_value = array[curr_index]
        insert_index = curr_index

        while insert_index >= 1 and array[insert_index - 1] > insert_value :
            array[insert_index] = array[insert_index-1]
            insert_index = insert_index - 1

        array[insert_index] = insert_value

    return array

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))