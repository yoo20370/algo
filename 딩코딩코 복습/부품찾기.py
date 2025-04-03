import sys 

N = int(sys.stdin.readline().rstrip())
store = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
order = list(map(int, sys.stdin.readline().split()))

store_set = set(store)

for curr in order :
    if curr in store_set :
        print("yes", end=" ")
    else :
        print("no", end=" ")
