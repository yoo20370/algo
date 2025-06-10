input = 20


def find_prime_list_under_number(number):

    # 각 3 ~ number까지 반복문을 돌면서, 자신보다 작은 값을 자신에게 나눠 나누어 떨어지지 않으면 result 배열에 삽입하도록 구현할 예정 
    # 첫 번째 반복문은 각 현재 숫자를 높여가는 것 
    # 두 번째 반복문은 현재 숫자를 나누는 연산을 수행 
    if number == 1 :
        return []
    if number == 2 :
        return [2]
    
    result = []
    result.append(2)

    curr_number = 3
    while curr_number <= number :
        for div in range(2, int(curr_number ** (1/2) + 1)) :
            if curr_number % div == 0 :
                break
        else :
            result.append(curr_number)
        
        curr_number += 1
    
    return result


result = find_prime_list_under_number(input)
print(result)

input = 20


# 에라토스테네스의 체 
def find_prime_list_under_number(number):
    # 일단 true, false 테이블을 만들어야 함, 해당 숫자가 소수라면 true 아니라면 false를 기록할 테이블 필요
    # 소수를 순회하면서 소수의 배수를 모두 제거한다. 
    
    prime_table = [True] * (number + 1)
    prime_table[0] = prime_table[1] = False

    # 소수를 순회하는 반복문 
    for curr_prime in range(2, int(number ** (1/2) + 1)) : 
        if prime_table[curr_prime] == True :

            # 소수의 배수인 수를 모두 테이블에 False로 기록 
            curr_multiple_value = 2
            while curr_prime * curr_multiple_value <= number :
                prime_table[curr_prime * curr_multiple_value] = False
                curr_multiple_value += 1
    
    result = []
    for index in range(2, number + 1) :
        if prime_table[index] == True :
            result.append(index)
    return result


result = find_prime_list_under_number(input)
print(result)