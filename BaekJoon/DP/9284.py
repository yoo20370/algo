import sys 

dpTable = [[[0] * 51 for i in range(51)] for i in range(51)]

def w(a, b, c) :


    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    
    if dpTable[a][b][c] != 0 :
        return dpTable[a][b][c]
    
    if a > 20 or b > 20 or c > 20 :
        if dpTable[20][20][20] == 0 :
            dpTable[20][20][20] = w(20,20,20)
        return dpTable[20][20][20]
    
    if a < b and b < c :
        if dpTable[a][b][c-1] == 0 :
            dpTable[a][b][c-1] = w(a, b, c-1)

        if dpTable[a][b-1][c-1] == 0 :
            dpTable[a][b-1][c-1] = w(a, b-1, c-1)
        
        if dpTable[a][b-1][c] == 0 :
            dpTable[a][b-1][c] = w(a, b-1, c)

        return dpTable[a][b][c-1] + dpTable[a][b-1][c-1] - dpTable[a][b-1][c]
    
    if dpTable[a-1][b][c] == 0 :
            dpTable[a-1][b][c] = w(a-1, b, c)

    if dpTable[a-1][b-1][c] == 0 :
            dpTable[a-1][b-1][c] = w(a-1, b-1, c)

    if dpTable[a-1][b][c-1] == 0 :
            dpTable[a-1][b][c-1] = w(a-1, b, c-1)

    if dpTable[a-1][b-1][c-1] == 0 :
            dpTable[a-1][b-1][c-1] = w(a-1, b-1, c-1)
    
    return dpTable[a-1][b][c] + dpTable[a-1][b-1][c] + dpTable[a-1][b][c-1] - dpTable[a-1][b-1][c-1]


while True :
    A, B, C = map(int, sys.stdin.readline().split())

    if A == -1 and A == B and A == C :
        break

    print(f"w({A}, {B}, {C}) = {w(A, B, C)}")

# import sys 

# dpTable = [[[0] * 51 for i in range(51)] for i in range(51)]

# def w(a, b, c) :


#     if a <= 0 or b <= 0 or c <= 0 :
#         return 1
    
#     if dpTable[a][b][c] != 0 :
#         return dpTable[a][b][c]
    
#     if a > 20 or b > 20 or c > 20 :

#         if dpTable[20][20][20] == 0 :
#             dpTable[20][20][20] = w(20,20,20)
#         return dpTable[20][20][20]
    
#     if a < b and b < c :

#         if dpTable[a][b][c-1] == 0 :
#             dpTable[a][b][c-1] = w(a, b, c-1)

#         if dpTable[a][b-1][c-1] == 0 :
#             dpTable[a][b-1][c-1] = w(a, b-1, c-1)
        
#         if dpTable[a][b-1][c] == 0 :
#             dpTable[a][b-1][c] = w(a, b-1, c)

#         return dpTable[a][b][c-1] + dpTable[a][b-1][c-1] + dpTable[a][b-1][c]
    
#     if dpTable[a-1][b][c] == 0 :
#             dpTable[a-1][b][c] = w(a-1, b, c)

#     if dpTable[a-1][b-1][c] == 0 :
#             dpTable[a-1][b-1][c] = w(a-1, b-1, c)

#     if dpTable[a-1][b][c-1] == 0 :
#             dpTable[a-1][b][c-1] = w(a-1, b, c-1)

#     if dpTable[a-1][b-1][c-1] == 0 :
#             dpTable[a-1][b-1][c-1] = w(a-1, b-1, c-1)
    
#     # w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
#     return dpTable[a-1][b][c] + dpTable[a-1][b-1][c] + dpTable[a-1][b][c-1] + dpTable[a-1][b-1][c-1]

# while True :
#     A, B, C = map(int, sys.stdin.readline().split())

#     if A == -1 and A == B and A == C :
#         break

#     print(w(A, B, C))