# 2 3 4 6 8 12 

# 24 


# 2 4 7 8 14 28 56 3307 6614 13228 23149 26456 46298 92596

import sys 

N = int(sys.stdin.readline().rstrip())
listA = list(map(int, sys.stdin.readline().split()))

listA.sort()

def func(n, arr) :
    if n == 1 :
        return arr[0] ** 2    
    return arr[0] * arr[n-1]

print(func(N, listA))
