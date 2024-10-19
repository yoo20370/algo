hour, minute = map(int , input().split())

def wakeUp45(hour, minute) :
    minute -= 45

    if minute < 0 : 
        minute = 60 + minute 
        hour -= 1
    
    if hour < 0 :
        hour = 23

    return hour, minute


hour, minute = wakeUp45(hour, minute)
print(hour, minute)