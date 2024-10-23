# 2 ~ 7 - 6
# 8 ~ 19 - 12
# 20 ~ 37 - 18
# 38 ~ 61 - 24
# 

N = int(input())

def beeHouse(n) :
    if n == 1 :
        return 1
    
    std = 1
    room = 1
    while n > std : 
        std += 6 * room
        room += 1
        
    return room 
    
print(beeHouse(N))