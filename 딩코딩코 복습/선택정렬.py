input = [4, 6, 2, 9, 1]

def selection_sort(array):
    
    # 가장 맨 앞 부터, 해당 위치에 들어올 원소를 확정시킨다.
    # 즉, 매 턴마다 가장 작은 값 혹은 가장 큰 값을 찾아서 확정시키면 된다.

    for i in range(len(array) - 1) :
        minIndex = i
        for j in range(i, len(array)) :
            if array[minIndex] > array[j] :
                minIndex = j
        array[minIndex], array[i] = array[i], array[minIndex]

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))