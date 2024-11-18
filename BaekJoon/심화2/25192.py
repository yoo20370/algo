import sys 

N = int(sys.stdin.readline().rstrip())
    
sum = 0
setA = set()
for i in range(N) :
    data = sys.stdin.readline().rstrip()
    if data == 'ENTER':
        sum += len(setA)
        setA.clear()
    else :
        setA.add(data)

sum += len(setA)
print(sum)
    