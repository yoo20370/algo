N, M = map(int, input().split())

def factorial(n) :
    if n == 1 :
        return 1

    return n * factorial(n-1)

def combination(n, m) :
    if m == 0 or n == m:
        return 1

    return factorial(n) // factorial(n-m) // factorial(m)

print(combination(N, M))