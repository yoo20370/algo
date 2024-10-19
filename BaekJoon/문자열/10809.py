string = input()

alpha = [-1] * 26

for i in range(len(string)) :
    if alpha[ord(string[i]) - 97] == -1 :
        alpha[ord(string[i]) - 97] = i
for i in alpha :
    print(i, end=" ")