import sys

N = int(sys.stdin.readline().rstrip())

dpTable = [0] * (N+1) 
cnt1 = 0
cnt2 = 0

def fib(n) :
    
    if n == 1 or n == 2 :
        return 1
    global cnt1 
    cnt1 += 1
    return fib(n-1) + fib(n-2)



def fibonacci(n, dpTable) :
    dpTable[1] = dpTable[2] = 1

    if dpTable[n] != 0 :
        return dpTable[n]
    global cnt2 
    cnt2 += 1
    dpTable[n] = fibonacci(n-1, dpTable) + fibonacci(n-2, dpTable)
    return dpTable[n]

fib(N)
fibonacci(N, dpTable)
print(cnt1 + 1, cnt2)

