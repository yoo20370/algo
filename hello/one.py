## 에라토스테네스의 체를 활용해야 빨리 풀 수 있다.
## 소수 목록 리스트를 만든다. 이때 아직 소수 목록을 모르기 때문에 모두 소수라고 가정하고 True로 초기화한다.
## 0, 1의 경우 False로 소수가 아님을 등록한다.
## 2부터 maxSize + 1 까지 순회하면서, 소수의 배수를 False로 만든다. (배수는 소수가 아니기 때문)
## maxSize까지 모두 할 필요가 없는 이유는 곱의 두 수를 중복해서 처리할 필요가 없기 때문 


input = 20


def find_prime_list_under_number(number):
    result = []

    maxSize = input + 1

    primeNumberList = [True] * maxSize

    primeNumberList[0] = primeNumberList[1] = False

    for number in range(2, int(maxSize ** 0.5) + 1) :
        if primeNumberList[number] == True :

            for currentNumber in range(number * number, maxSize, number) :
                primeNumberList[currentNumber] = False

    for number in range(maxSize) :
        if primeNumberList[number] == True :
            result.append(number)

    return result


result = find_prime_list_under_number(input)
print(result)