def factorial(n):
    # 종료조건 
    if n == 1 : 
        return 1 

    # 문제 축소 
    return n * factorial(n-1)

print(factorial(5))