# 곱하거나 더하기
# 들어오는 값이 0 혹은 1인 경우 더하기
# 예외 - 만약 현재 합이 0이거나 1이면 반드시 합 

def find_max_plus_or_multiply(array):

    totalValue = 0

    for currentNumber in array : # O(N)

        if currentNumber <= 1 or totalValue <= 1 :
            totalValue += currentNumber
            continue

        totalValue *= currentNumber
    
    return totalValue


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))