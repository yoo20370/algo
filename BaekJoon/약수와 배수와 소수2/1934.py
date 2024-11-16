# import sys 
# N = int(sys.stdin.readline().rstrip())

# def func(num1, num2) :
#     # 둘 중 하나라도 1이라면 곱하면 된다.
#     if num1 == 1 or num2 == 1 :
#         return num1 * num2 
    
#     x = num1
#     y = num2

#     s1 = 1
#     s2 = 1

#     while x != y :
#         if x < y :
#             s1 += 1
#             x = num1 * s1
#         else :
#             s2 += 1
#             y = num2 * s2
    
#     return x

# for i in range(N) :
#     x, y = map(int, sys.stdin.readline().split())
#     print(func(x, y))

import sys

# 소인수 구하기 
def func1(n) :
    setA = set()
    if n < 4 :
        setA.add(n)
        return setA
    
    for i in range(2, (n+2) // 2) :
        if n % i == 0 :
            a = func2(i) 
            b = func2(n // i)

            if a == True :
                setA.add(i)
            if b == True :
                setA.add(n // i)
    
    return setA

# 소수를 구하는 함수
def func2(n) :
    if n == 1 :
        return False
    elif n < 4 :
        return True
    
    if n % 2 == 0 :
        return False

    for i in range(3, (n+2) // 2, 2) :
        if n % i == 0 :
            return False

    return True

def func3(n) :
    listA = list(func1(n))
    if len(listA) == 0 :
        return -1
    listA.sort()    
    resultList = list()

    max_idx = len(listA) - 1
    s_idx = 0
    i = listA[s_idx]
    while n != i :
    
        # 다음 소인수로 계산 진행 
        if n % i != 0 and s_idx <= max_idx :
            s_idx += 1
            i = listA[s_idx]
            continue
        elif s_idx > max_idx :
            break

        resultList.append(i)
        n = n // i
    resultList.append(i)

    return resultList

    ## 두 수 중 하나가 1이거나 소수인 경우 상대방과 그대로 곱한다. 

def mainFunc(num1, num2) :

    if num1 == 1 or num2 == 1 or func2(num1) == True or func2(num2) == True :
        return num1 * num2
    # listA = func3(num1)
    # listB = func3(num2)

    # setA = set(listA)
    # setB = set(listB)

    # setHap = setA | setB
    # print(setHap)
    x = num1
    y = num2

    s1 = 1
    s2 = 1

    while x != y :
        if x < y :
            s1 += 1
            x = num1 * s1
        else :
            s2 += 1
            y = num2 * s2
    
    return x

N = int(sys.stdin.readline().rstrip())
for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    print(mainFunc(x, y))