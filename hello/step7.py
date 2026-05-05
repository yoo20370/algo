# • 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다. 
#   단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다. 1. N에서 1을 뺍니다. 2. N을 K로 나눕니다. 
# • 예를 들어 N이 17, K가 4라고 가정합시다. 이때 1번의 과정을 한 번 수행하면 N은 16이 됩니다. 
#   이후에 2번의 과정을 두 번 수행하면 N은 1이 됩니다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 됩니 다. 이는 N을 1로 만드는 최소 횟수입니다. 
# • N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그 램을 작성하세요.

# 현재 값이 1인가 ? 
# 현재 값이 나누어 떨어지는가 ?? 
# 현재 값을 K로 나눈 뒤 다시 그 K를 곱하고 빼야하는 횟수를 구한다. 
# Ex) 24, 5 -> 24 / 5 -> 4 -> 4 * 5 = 20 -> 24 - 20 -> 4번 1 감소 -> count
# 다시 처음으로 돌아간다. 

# 지금 놓친 게 있음, 그걸 찾아야 함 



# 24, 5
# 24 -> 20 || (4)
# 20 -> 4 || (5)
# 4 -> 1 || (8)

import sys

def solution() :
    N, K = map(int, sys.stdin.readline().split())

    currentValue = N 
    count = 0

    while currentValue != 1 :

        # 나누어 떨어지지 않는 경우, 
        if currentValue % K != 0 :
            
            # 몫이 없는 경우 
            if currentValue < K :
                count += currentValue - 1
                
                break

            result = currentValue // K 
            temp = result * K 

            count += currentValue - temp
            currentValue = temp
            
        else :
            result = currentValue // K 
            count += 1
            currentValue = result
        
    return count

print(solution())