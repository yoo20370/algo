# 1이 될 때까지 두 가지 가능 
# N에서 1을 뺄 수 있다.
# N을 K로 나눈다. 

# 일단 나누어 떨어지지 않으면 뺄거야 -> 카운트 (N - (N // K) * K) -> 더할 개수 
# 나누어 떨어지면 나눌거야 -> 나머지를 다음 값으로 다음 작업 수행 -> 나누었을 때 몫이 0이면 끝나야 함 
# 언제까지 수행해야 하지 ?? 1이 될 때 까지 

import sys 

N, K  = map(int, sys.stdin.readline().split())

totalCount = 0

currentNumber = N 

# 만약 같으면 몫이 1이니까 문제 없음 
while currentNumber >= K :
    
    # 나누어 떨어지지 않는 경우 
    if currentNumber % K != 0 :
        minusCount = currentNumber - currentNumber // K * K
        totalCount += minusCount

        currentNumber -= minusCount

    # 나누어 떨어지는 경우 
    else :
        totalCount += 1 
        currentNumber = currentNumber // K

if currentNumber != 1 :
    totalCount += currentNumber - 1

print(totalCount)  

    

