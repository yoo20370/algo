# 소수 구하기 
# 소수라는 것은 1과 본인을 제외한 나머지 숫자로 나누어 떨어지면 안 되는 수 
# M 이상, N 이하의 소수를 모두 출력 

## 3 ~ 16이라고 했을 때 3부터 소수인지 파악하면 됨 
### 소수 판별 메서드가 있으면 좋을 것 같음 

## 에라토스테네스의 체 
## 배열로 만들어야 함 prime 목록을 만들어야 함 
## 2가 만약 소수가 아니라면 2의 배수는 소수가 아님 
## 그리고 그 다음 소수가 아닌 수를 찾아서 제거해가는 방법

### 2 3 4 5 7 9
# 합성수는 항상 √N보다 작은 약수를 하나 갖는다
import sys

M, N = map(int, sys.stdin.readline().split())

primeList = [True] * (N + 1)

primeList[0] = primeList[1] = False

for currentNumber in range(2, int(N ** 0.5) + 1) :
    if primeList[currentNumber] :

        multiValue = currentNumber
        while currentNumber * multiValue <= N :
            primeList[currentNumber * multiValue] = False
            multiValue += 1
    


for index in range(M, N + 1) :
    if primeList[index] :
        print(index)


    
        
        
        
        









