input = 20

def fibo_recursion(number):


    memory = [-1] * (number + 1)
    memory[0] = 0
    memory[1] = 1

    for n in range(2, number + 1) :
        memory[n] = memory[n-1] + memory[n-2]

    return memory[number]

print(fibo_recursion(input))  # 6765