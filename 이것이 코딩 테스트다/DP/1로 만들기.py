import sys 

N = int(sys.stdin.readline().rstrip())

def makeOne(n) :
    if n == 1 :
        return 0
    cnt = 0 
    while n != 1 :
        cnt += 1
        if n % 5 == 0 :
            n = n // 5 
        elif n % 3 == 0 :
            n = n // 3
        elif n % 2 == 0 :
            n = n // 2
        else :
            n -= 1
        
        print(n)
        
    print(cnt)

print(makeOne(N))