start, m, d, n = map(int, input().split())

step = 1
while step < n :
    step += 1
    start *= m 
    start += d
print(start)