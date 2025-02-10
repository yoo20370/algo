input = [4, 6, 2, 9, 1]

def bubble_sort(array):

    # 바깥 반복문은 끝에서 저장해야할 offset을 설정
    # 안쪽 반복문은 인접한 원소를 비교하기 위한 인덱스 1부터 시작하는 이유는 이전 원소와 현재 원소를 비교하기 위함, len(array) - i을 수행하는 이유는 확정 지을 위치를 위함

    array_length = len(array_length)

    for i in range(array_length - 1) : 
        for j in range(1, array_length - i) :
            if array[j-1] > array[j] :
                array[j-1], array[j] = array[j], array[j-1]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))