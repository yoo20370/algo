import sys

total = 0
while True :
    data = int(sys.stdin.readline().rstrip())
    if data == -1 :
        break
    total += data

print(total)