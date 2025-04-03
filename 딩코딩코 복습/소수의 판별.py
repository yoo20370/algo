# 숫자 n이 주어졌을 때, 모든 소수 목록을 출력하기
import sys

number = int(sys.stdin.readline().rstrip())

# # 기본적인 약수를 구하는 함수 
# def get_prime_numbers(target) :
#     result_list = [2]

#     # 숫자 3부터 target 숫자까지 다음의 과정을 반복한다.
#     # 특정 숫자가 소수인지 판별하려면 특정 숫자보다 작은 수로 특정 숫자로 모두 나누어 나누어 떨어지는지 확인
#     # 이 때, N X M 형태가 나오므로 중앙 숫자까지만 연산을 수행하면 된다. 

#     for i in range(3, target+1) :
        
#         for j in range(2, int(i**(1/2)) + 1) :
#             if i % j == 0 :
#                 break
#         else :
#             result_list.append(i)

#     return result_list

# print(get_prime_numbers(number)) 

def get_prime_numbers(number) :

    prime_list = [True] * (number + 1)
    prime_list[0] = prime_list[1] = False
    
    for curr_prime_number in range(int(len(prime_list) ** (1/2)) + 1) :

        if prime_list[curr_prime_number] :
            for value in range(curr_prime_number * curr_prime_number, number + 1, curr_prime_number) :
                prime_list[value] = False

    for index in range(len(prime_list)) :
        if prime_list[index] == True :
            print(index, end=" ")

get_prime_numbers(number)
