import sys

N = int(sys.stdin.readline().rstrip())

count = 0
for hour in range(0, N + 1) :
    for minute in range(0, 60):
        for second in range(0, 60):
            if "3" in str(hour) + str(minute) + str(second) :
                count += 1
print(count)
