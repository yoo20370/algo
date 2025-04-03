def find_max_plus_or_multiply(array):
    # 현재 값이 0이거나 곱하는 값이 0인 경우 무조건 더해준다.
    # 현재 값이 1이거나 곱하는 값이 1이라면 더 해준다. 
    sum = 0 # 1
    for currNum in array : # n
        if sum <= 1 or currNum <= 1 : # 1
            sum += currNum  # 1
        else :
            sum *= currNum

    return sum

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))