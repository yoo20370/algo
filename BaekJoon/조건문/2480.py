A, B, C = map(int, input().split())

def check(A, B, C) :

    if A == B and B == C :
        return 10000 + A * 1000
    elif (A == B and A != C) or (A == C and A != B ): 
        return 1000 + A * 100
    elif (B == C and A != B) :
        return 1000 + B * 100
    else :
        maxVal = max(A, B, C)
        return maxVal * 100
    
print(check(A,B,C))
    
        