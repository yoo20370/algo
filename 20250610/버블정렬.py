input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 버블 정렬이란, 인접한 원소끼리 비교하며 정렬을 수행하는 정렬 알고리즘으로 재자리 정렬, 안정정렬이다.
    # 바깥쪽 반복문의 인덱스는 안쪽 반복문의 이동 인덱스를 계산하기 위한 인덱스
    # 안쪽 반복문은의 인덱스는 인덱스를 이동하면서 인접한 요소의 값을 비교하기 위한 인덱스 
    for i in range(1, len(array)) :
        for j in range(len(array) - i) :
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    
    return array

bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))