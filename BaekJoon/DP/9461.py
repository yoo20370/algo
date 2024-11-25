import sys 

dpTable = [0] * 101
dpTable[1] = 1
dpTable[2] = 1
def pado(n) :

    if n < 4 :
        return 1
    
    if dpTable[n-3] == 0 :
        dpTable[n-3] = pado(n-3)

    if dpTable[n-2] == 0 :
        dpTable[n-2] = pado(n-2)

    return dpTable[n-3] + dpTable[n-2] 

N = int(sys.stdin.readline().rstrip())

for i in range(N) :
    K = int(sys.stdin.readline().rstrip())
    print(pado(K))


