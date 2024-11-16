import sys

setA = set()

string = sys.stdin.readline().rstrip()

# i는 길이
for i in range(1, len(string) + 1) :
    # 인덱스 위치
    for j in range(0,len(string) - i + 1) :
        setA.add(string[j:j+i])

print(len(setA))



