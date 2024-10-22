N = int(input())

for i in range(1, N+1) :
    print(" " * (N -i), end="")
    print("*" * (2*i-1))
    

for i in range(N-1, 0, -1) :
    print(" " * (N -i), end="")
    print("*" * (2*i-1))
    

# 별은 증가하고 공백은 감소 
# 별 1개 공백 0개

# 별 3개 공백 2개 

# 별 5개 공백 4개 

# 별 9개 공백 8개 

# 별 11개 공백 10개

# 별의 개수는 2N-1

