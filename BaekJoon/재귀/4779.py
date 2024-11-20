def func(data) :

    size = len(data)
    if size == 1 :
        return "-"

    l = size // 3
    r = (size * 2) // 3

    return func(data[:l]) + (r - l) * ' ' + func(data[r:])
    

while True :
    try :
        N = int(input())
        size = 3 ** N

        if N == 0 :
            print("-")
        else :
            print(func("-"*size))
    
    except EOFError :
        break
    