a, d, n = map(int, input().split())

step = 1
start = a
while step != n :
    step += 1
    start += d

print(start)