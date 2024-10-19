sum = int(input())
N = int(input())

sum2 = 0
for i in range(N) :
    val, cnt = map(int, input().split())
    sum2 += val * cnt

if sum == sum2 :
    print("Yes")
else :
    print("No")