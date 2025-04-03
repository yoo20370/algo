input = [4, 6, 2, 9, 1]

# n-1까지 수행하면 됨 

def bubble_sort(array):
    # 첫 번째 원소부터 시작해서 이웃을 비교해가며 마지막 원소를 확정시킨다.
    # 즉, 비교하는 원소의 수가 줄어야 한다. 
    for i in range(len(array) - 1) :
        swapped = False
        for j in range(len(array) - 1 - i) :
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped :
            break
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))