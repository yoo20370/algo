import sys

def hanoi(n, start, sub, end) :
    
    if n > 1 :
        hanoi(n-1, start, end ,sub) 
    print(start, end)
    if n > 1 :
        hanoi(n-1, sub, start, end)  

N = int(sys.stdin.readline().rstrip())

print(2**N - 1)
hanoi(N,1,2,3)
