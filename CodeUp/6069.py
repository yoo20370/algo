start, r, n = map(int, input().split())

step = 1
while step < n  :
    step += 1
    start *= r
print(start)