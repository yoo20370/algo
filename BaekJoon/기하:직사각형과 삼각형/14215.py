listA = list(map(int, input().split()))

listA.sort(reverse=True)

x, y, z = listA

if x >= y + z :
    x = y + z - 1

print(x + y + z)


