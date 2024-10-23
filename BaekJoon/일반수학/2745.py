N, B = input().split()

length = len(N) 

sum = 0
for i in range(length) :    

    curr = N[length-1-i]
    if curr.isdigit() :
        curr = int(curr)
    else : 
        curr = ord(curr) - 55 
    
    sum += curr * int(B)**i
print(sum)
