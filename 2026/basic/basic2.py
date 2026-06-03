# 가장 큰 수를 구해야 한다.
## 값이 0인 경우 그냥 더한다. (곱하면 0이 됨)
## 값이 1인 경우 그냥 더하는게 좋음 (곱해봤자 그대로 혹은 0이면 0이 되기 때문)
## 현재 sum 값이 0이거나 1인 경우도 더한다. 

def find_max_plus_or_multiply(array):

    total = 0

    for number in array :

        if total <= 1 or number <= 1 :
            total += number 

        else :
            total *= number
    
    return total


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))