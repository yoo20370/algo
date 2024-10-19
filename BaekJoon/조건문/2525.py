def finishTime(hour, minute, time) :
    minute += time 

    while minute >= 60 :
        if minute >= 60 :
            hour += 1
            minute -= 60

    if hour >= 24 :
        hour = hour - 24

    return hour, minute 

hour, minute = map(int, input().split())    
time = int(input())

hour, minute = finishTime(hour, minute, time)
print(hour, minute)
