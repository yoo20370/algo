def find_max_num(array):
    # 최대값 찾기 
    # 최대값 변수를 생성하고 배열의 첫 번째 값을 최대값으로 설정한다.
    # 배열을 순회하면서 최대값보다 크다면 최대값 변수에 값을 넣는다. 
    
    # 전체 시간복잡도 O(N)
    max_value = array[0] # O(1)
    array_length = len(array) #O(1)

    for i in range(1, array_length) : # O(n-1)
        if max_value < array[i] : max_value = array[i] #O(1)

    return max_value # O(1)


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))