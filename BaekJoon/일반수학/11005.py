# N, B = map(int, input().split())

# i = 0
# while True :
    
#     if N < B ** (i+1) :
#         break
#     i += 1

# string = ""
# for i in range(i, -1, -1) :
#     result = N // (B**i)
#     N = N % (B**i)
    
#     if result > 9 :
#         result = chr(result+55)

#     string += str(result)

# print(string)

N, B = map(int, input().split())

result = ""
while N > 0 :
    R = N % B 
    result += (chr(R+55) if R > 9 else str(result))
    N = N // B
print(result)