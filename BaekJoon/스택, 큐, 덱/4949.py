import sys

def check(s) :
    p1 = 0
    p2 = 0

    for i in s :
        if i == '(' :
            p1 += 1
        elif i == ')' :
            if p1 != 0 :
                p1 -= 1
            else :
                return "no"
        elif i == '[' :
            p2 += 1 
        elif i == ']' :
            if p2 != 0 :
                p2 -= 1
            else :
                return "no"

    if p1 == 0 and p2 == 0 :
        return "yes"
    else :
        return "no"

while True :
    data = sys.stdin.readline().rstrip()
    if data == '.' :
        break
    
    print(check(data))
    
            

