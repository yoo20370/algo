import sys

N = int(sys.stdin.readline().rstrip())

data = []
for _ in range(N) :
    name, score = sys.stdin.readline().split()
    data.append((name, int(score)))

data.sort(key=lambda x : (-x[1], x[0]), reverse=True)

for name, score in data :
    print(name, end = " ")