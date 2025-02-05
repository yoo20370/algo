import sys 

N = int(sys.stdin.readline().rstrip())

for _ in range(N) :

    num = int(sys.stdin.readline().rstrip())
    
    for i in range(2, 1000001) :
        if num % i == 0 :
            print("NO")
            break
        if i == 1000000 :
            print("YES")