# numbers = [1,2,3,4,5,6,7,8,9,10,11]

# # 소수 구하기

# def prime_check(n) -> bool :

#     if n == 1 : 
#         return False
    
#     if n in (2, 3) : 
#         return True
    
#     for i in range(2, int(n**0.5) + 1) : # O(N**0.5)
#         if n % i == 0 :
#             return False
        
#     return True

# for number in numbers :
#     if prime_check(number) :
#         print(number, end=" ")

# 에라토스테네스의 체 
# 특정 범위의 수에 대하여 빠르게 소수들을 찾아내는 방법 

# 소수인지 아닌지 체크하는 배열을 만든다.
# 소수인 수를 차례대로 접근해서 소수의 배수인 수들을 소수가 아님으로 배제한다.

def prime_check(n) -> None :

    prime_check_array = [True] * (n + 1)

    prime_check_array[0] = prime_check_array[1] = False

    for curr_prime in range(2, int(n ** 0.5) + 1) :

        if prime_check_array[curr_prime] == True :
            for multi in (curr_prime * curr_prime, n + 1, curr_prime) :
                prime_check_array[multi] = False

    for i in range(1, len(prime_check_array)) :
        if prime_check_array[i] :
            print(i, end=" ")

prime_check(100)   


