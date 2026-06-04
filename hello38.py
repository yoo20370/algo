# 소수 구하기
# 에라토스테네스의 체로 풀어봐야 함 -> 그 소수 구하기가 애초에 안에 있기 때문 
# 시간복잡도 여유가 있다면 -> 단순 소수 구하기면 충분
# 그렇지 않다면 에라토스테네스의 체를 통해 빠르게 구할 필요가 있음 
# 소수가 아닌 수를 지워나가는 방식 

# prime이라는 배열에 소수인 수를 기록한다.
# 소수인 경우 배수라 판단하여 소수의 배수를 모두 primeList에서 지운다.
# 현재 number가 소수인지 확인한 후, 소수인 경우 실행하면 될 것 같다.


input = 20


def find_prime_list_under_number(number):

    primeList = [True] * (number + 1) 
    # 소수가 아님 
    primeList[0] = False
    primeList[1] = False

    # 합성수는 배수에 의해 제거되기 때문에 제곱근까지만 확인하면 됨 
    for number in range(2, int(len(primeList) ** 0.5) + 1) :

        if primeList[number] :
            # number * number 부터 시작하는 이유 -> number 이전의 값들이 이미 처리했기 때문 
            for i in range(number * number, len(primeList), number) :
                primeList[i] = False
    
    result = []
    for number in range(1, len(primeList)) :
        if primeList[number] :
            result.append(number)

    return result


result = find_prime_list_under_number(input)
print(result)