input = [4, 6, 2, 9, 1]

# 버블 정렬은 이웃한 녀석들끼리 비교하는 것 
# 맨 뒤를 확정짓게 하자 
# 그럼 바깥 반복문은 마지막 인덱스 - 바깥 반복문 변수값 이런 식으로 해서, 뒤 부터 확정 짓는 걸로 하자
# 내부 반복문은 N - 1, N - 2, N - 3 이런 식으로 비교해야 함
# 즉, 외부 반복문의 변수를 값을 이용해서 제어해야 할 것 같음 

def bubble_sort(array):
    
    length = len(array)

    for i in range(length - 1) :
        for j in range(0, length - i - 1, 1) :
            if array[j + 1] < array[j] :
                array[j + 1], array[j] = array[j], array[j + 1]
    
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))