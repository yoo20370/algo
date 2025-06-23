# 0 ~ 9 사이의 숫자로 이뤄진 문자열 S가 있을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 곱 혹은 더하기 연산만 가능
## 가장 큰 수를 구하여라 

# 합계가 0이거나 1인 경우 더한다. 또한 더하는 수가 0이거나 1이면 무조건 더한다. 

import sys 

def solution() :
     
    sum_value = 0
    for curr_value in sys.stdin.readline().rstrip() :
        
        curr_value = int(curr_value)
        if sum_value <= 1 or curr_value <= 1 :
            sum_value += curr_value
        else :
            sum_value *= curr_value

    
    return sum_value

print(solution())
