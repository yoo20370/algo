# 소수 찾기

# 결국 만들 수 있는 모든 숫자를 나열하고
# 모든 수에 대하여 소수인지 확인해야 할 것 같음

# 순열을 이용해서 가능한 모든 숫자를 만들어야 함 -> 방법을 구하는게 아니고 숫자이기 때문 
# 여기서 고민해봐야 할 게 모든 숫자가 있을 때, 각각에 대해서 소수인지 확인하는 것이 좋을지
# 아니면 에라토스테스의 체를 통해서 가장 큰 값까지 모든 수에 대해서 소수인지 구한뒤 반환하는게 카운트하는게 좋을지 

# 생각 해보자 
# 각각에 대해서 소수인지 확인하는 방법은 
# int(9876543 ** (0.5)) * N! 
# 9999999의 제곱근 만큼 비교하여 현재 값이 소수인지 확인
# N!는 가능한 최대 순열 시간복잡도

## 어떻게 풀건가 ??
## permutations을 통해서, 순열로 가능한 경우를 확인
## 이들을 하나로 만들어서 숫자로 생성
## 만약 해당 숫자에 대해서 소수 확인을 하지 않았다면 
## count 함

## 0과 1을 소수가 아니므로 처리되지 않도록 하고, 중복 체크하지 않도록 함 

from itertools import permutations

def isPrimeNumber(number) :
    
    for i in range(2, int(number ** (0.5)) + 1) :
        if number % i == 0 :
            return False
    
    return True 

def solution(numbers):
    
    isChecked = set()
    
    isChecked.add(0)
    isChecked.add(1)
    count = 0
    for i in range(1, len(numbers) + 1) :
        for x in permutations(numbers, i) :
            currentNumber = int("".join(x))
            
            if currentNumber not in isChecked :
                if isPrimeNumber(currentNumber) :
                    isChecked.add(currentNumber)
                    count += 1
    
    return count