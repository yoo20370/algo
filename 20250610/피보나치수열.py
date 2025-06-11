# Top_down 방식
input = 20

dp_table = [0] * (input + 1)
dp_table[0] = 0
dp_table[1] = 1
def fibo_recursion(n):

    if n < 2 :
        return dp_table[n]
    
    if dp_table[n] != 0 :
        return dp_table[n]
    
    dp_table[n] = fibo_recursion(n-1) + fibo_recursion(n-2)
    return dp_table[n]


print(fibo_recursion(input))  # 6765

# bottom_up 방식
input = 20

dp_table = [0] * (input + 1)
dp_table[0] = 0
dp_table[1] = 1
def fibo_recursion(n):

    if n < 2 :
        return dp_table[n]
    
    for i in range(2, input + 1) :
        dp_table[i] = dp_table[i-1] + dp_table[i-2]

    return dp_table[n]

print(fibo_recursion(input))  # 6765