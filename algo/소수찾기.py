# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 함 
# 길이가 7이하 이므로 모든 경우의 수를 고려할 수 있을 것 같음 -> 순열 permutation
# 소수인지 판별하는 메서드를 만들고, 모든 경우의 수에 대하여, 소수인지 판별하도록 한다. 
# 시간 복잡도가 많이 소요될 것 같으면 에라토스테니스의 체를 사용한다. 
import itertools
def is_prime(number):
    
    if number <= 1 :
        return False
    
    for i in range(2, int(number ** (1/2)) + 1) :
        if number % i == 0 :
            return False
    return True
 
def solution(numbers):
    
    numbers = [ch for ch in numbers]
    
    result = set()
    for length in range(1, len(numbers) + 1) :
        for x in itertools.permutations(numbers, length) :
            number = int("".join(x))
            if is_prime(number) :
                result.add(number)
                
    print(result)
    return len(result)