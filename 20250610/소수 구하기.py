import sys 

# 에라토스테네스의 체를 이용해서 풀어보자
# 소수를 기록한 테이블을 만든다. 
# 외부 반복문은 소수를 선택하는 반복문 
# 내부 반복문은 소수의 배수로 소수 테이블에 접근하여 소수가 아닌 수를 제거하자 

start, end = map(int, sys.stdin.readline().split())

prime_table = [True] * (end + 1) 
prime_table[1] = False

for prime_number in range(2, int(end**(1/2)) + 1) :
    if prime_table[prime_number] :

        value = 2 
        while prime_number * value <= end :
            prime_table[prime_number * value] = False
            value += 1

for index in range(start, len(prime_table)) :
    if prime_table[index] == True :
        print(index)

