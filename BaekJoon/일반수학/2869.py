A, B, V = map(int, input().split())

final = V - A 
C = A - B 

if final % C != 0 :
    print(final // C + 2)
else :
    print(final // C + 1) 