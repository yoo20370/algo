data = input()

list = [0] * 26

for i in data :
    idx = ord(i) - 97
    list[idx] += 1

for i in list :
    print(i, end=" ")

