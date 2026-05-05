input = 20

memory = [-1] * (input + 1)
memory[0] = 0
memory[1] = 1

def fibo_recursion(n):

    if n <= 1 :
        return memory[n]
    
    if memory[n] != -1 :
        return memory[n]
    
    memory[n] = fibo_recursion(n - 1) + fibo_recursion(n - 2)
    
    return memory[n]


print(fibo_recursion(input))  # 6765