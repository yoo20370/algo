N = input()

result = ''

for j in range(9, -1,-1) :
    for i in range(len(N)) :
        if N[i] == str(j) :
            temp = str(j)
            result += temp

print(result)