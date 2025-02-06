input = 20


def find_prime_list_under_number(number):
    
    # 2, 3을 결과 리스트에 넣는다.
    # 4부터 본인보다 작은 값으로 나눠본다. 그래서 만약 나눠지면 소수가 아니고
    # 나눠지지 않으면 소수 
    result = [2,3]

    # O(N^2)
    for curr_num in range(4, number+1) :

        check = 0 
        for check_num in range(2, int(curr_num ** 0.5) + 1) :
            if curr_num % check_num == 0 :
                check = 1 
                break
        if check == 0 :
            result.append(curr_num)

    return result


result = find_prime_list_under_number(input)
print(result)

