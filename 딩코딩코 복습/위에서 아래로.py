import sys 

N = int(sys.stdin.readline().rstrip())

data = []
for _ in range(N) :
    data.append(int(sys.stdin.readline().rstrip()))

for curr in sorted(data, reverse=True) :
    print(curr, end=" ")