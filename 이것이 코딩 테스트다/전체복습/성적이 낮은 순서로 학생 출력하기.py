import sys

N = int(sys.stdin.readline().rstrip())

studentScore = list()
for _ in range(N) :
    name, score = sys.stdin.readline().split()
    studentScore.append([name, int(score)])

studentScore.sort(key=lambda x : (x[1]))

for name, score in studentScore :
    print(name, end=" ")

