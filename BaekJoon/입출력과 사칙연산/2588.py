first = input()
second = input()

for j in range(len(second)-1, -1, -1 ):
    print(int(first) * int(second[j]))

print(int(first) * int(second))