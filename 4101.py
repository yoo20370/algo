import sys 
while True :

    N, M = map(int, sys.stdin.readline().split())

    if N == 0 and M == 0 :
        break

    if N > M :
        print("Yes")
    else :
        print("No")
    
