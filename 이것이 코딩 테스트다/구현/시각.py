import sys

N = int(sys.stdin.readline().rstrip())

hour = 0
minute = 0
second = 0 
cnt = 0
while N + 1 != hour :
    minute = 0
    
    while minute != 60 :
        second = 0

        while second != 60 :
            time = str(hour) + str(minute) + str(second)
            if '3' in time :
                cnt += 1
            second += 1
        minute += 1

    hour += 1

print(cnt)