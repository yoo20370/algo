x = int(input())
y = int(input())

def fourArea(x,y) :
    if x > 0 and y > 0 :
        return 1
    elif x < 0 and y > 0 :
        return 2
    elif x < 0 and y < 0 :
        return 3
    elif x > 0 and y < 0 :
        return 4
    else :
        return 0
    
print(fourArea(x,y))
