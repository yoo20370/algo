import sys 

N = int(sys.stdin.readline().rstrip())

for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())

    if x >= y :
        print("MMM BRANIS")
    else :
        print("NO BRAINS")