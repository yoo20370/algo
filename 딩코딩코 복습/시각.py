import sys

N = int(sys.stdin.readline().rstrip())

count = 0
for hour in range(N+1) :
    for minute in range(60):
        for second in range(60):
            time = str(hour) + str(minute) + str(second)
            if str(N) in time :
                count += 1 

print(count)