# 더하거나 곱하거나 
# 배열을 순회하며 더하거나 곱해서 최대값을 만들어야 한다.
# 값이 0이거나 1인 경우에 대해서 다르게 처리해야함 
# 합이 0이거나 원소가 0인 경우 반드시 더 한다.
# 합이 1이거나 원소가 1인 경우도 반드시 더 한다. 
def find_max_plus_or_multiply(array):
    
    totalCost = 0
    for number in array :
        if number <= 1 or totalCost <= 1:
            totalCost += number

        else : 
            totalCost *= number

    return totalCost


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))