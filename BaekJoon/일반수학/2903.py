N = int(input())

def cma(n) :
    
    if n == 1 :
        return 9 
    return cma(n-1) * 4 - 3 - 4 * (2**(n-1))

print(cma(N))