import sys

N = int(sys.stdin.readline().rstrip())
bring_item = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
order_item = list(map(int, sys.stdin.readline().split()))

for item in order_item :
    if item not in bring_item :
        print(0)
    else :
        print(1)
