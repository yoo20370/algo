dpTable = [0] * 100
dpTable[0] = dpTable[1] = 1
N = int(input())
def fatorial(n) :
    if n <= 1 :
        return 1
    
    if dpTable[n] != 0 :
        return dpTable[n]
    
    dpTable[n] = n * fatorial(n-1) 
    return dpTable[n]
    
print(fatorial(N))