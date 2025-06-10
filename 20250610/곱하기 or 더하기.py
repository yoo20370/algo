def find_max_plus_or_multiply(array):
    # 왼쪽부터 + 또는 x를 통해 가장 큰 값을 만들어야 한다. 
    # 만약 sum 값이나, 곱하는 값이 0이거나 1이면 더하기를 수행한다. 
    # 나머지는 곱하기를 수행한다. 
    # 또 다른 예외가 있으려나 ?
    # 단순히 배열을 순회하면서 더하거나 곱하면 되므로 O(N) 시간복잡도 소요 예정

    sum = 0 

    for curr in array :
        if sum <= 1 or curr <= 1 :
            sum += curr
        else :
            sum *= curr
    return sum


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))