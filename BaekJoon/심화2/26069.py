import sys

N = int(sys.stdin.readline().rstrip())

danceUsers = set()
danceUsers.add("ChongChong")
for i in range(N) :
    x, y = sys.stdin.readline().split()

    if x in danceUsers or y in danceUsers :
        danceUsers.add(x)
        danceUsers.add(y)
    
print(len(danceUsers))
    






