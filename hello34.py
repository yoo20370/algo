# 최대값을 구해야 함 
# 다른 것 없이 순회해서 찾으면 될 것 같음 -> O(N)

def find_max_num(array):
    
    maxValue = array[0]

    for index in range(1, len(array)) :
        if maxValue < array[index] :
            maxValue = array[index]

    return maxValue


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))