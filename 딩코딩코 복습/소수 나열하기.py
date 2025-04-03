input = 20


# def find_prime_list_under_number(number): # O(N * N ** 0.5) 

#     # 3부터 ~ number까지 순회 
#     # 2부터 현재Num - 1까지 나눠서 나누어 떨어지면 소수가 아님
#     # 나누어 떨어지지 않는다면 소수이므로 결과 리스트에 저장 

#     if number < 2 :
#         return []
    
#     result = [2]

#     for currNum in range(3, number+1) :  # N

#         for num in range(2, int(currNum ** 0.5) + 1) : # N ** 0.5 
#             if currNum % num == 0 :
#                 break
#         else :
#             result.append(currNum)

#     return result
    
input = 20

def find_prime_list_under_number(number):
    # 에라토스테네스의 체 
    # 가장 작은 소수를 선택하고 이 수를 이용해서 나누어 떨어지는 수를 후보에서 제거한다. 
    result = []

    primeArray = [True] * (number + 1)
    primeArray[0] = primeArray[1] = False

    # N * M 형태이므로 절반에 대해서만 수행하면 되기 떄문
    for currPrime in range(2, int(number ** 0.5) + 1) :
        if primeArray[currPrime] :
            
            for currNum in range(currPrime * currPrime, number + 1, currPrime) :
                primeArray[currNum] = False

    for idx in range(2, number + 1) :
        if primeArray[idx] == True :
            result.append(idx)

    return result


result = find_prime_list_under_number(input)
print(result)

