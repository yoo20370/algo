input = 20


def find_prime_list_under_number(number):
    
    # 2, 3을 결과 리스트에 넣는다.
    # 4부터 본인보다 작은 값으로 나눠본다. 그래서 만약 나눠지면 소수가 아니고
    # 나눠지지 않으면 소수 
    result = []

    # N 보다 작은 작은 소수들만 가지고 나누어 떨어지는지 비교하면 된다. 

    for curr_num in range(2, number+1) :

        check_flag = False
        for curr_prime in result :
            if curr_prime * curr_prime <= curr_num and curr_num % curr_prime == 0 :
                check_flag = True
                break
        if check_flag == False :
            result.append(curr_num)

    return result

result = find_prime_list_under_number(input)
print(result)

