import sys 

# 즉, 나누어 떨어지지 않는다면 1을 빼는 과정을 반복, 나누어 떨어지기 전의 1 빼는 작업을 반복문이 아닌 단순 연산으로 대체 
# 우선 K 값을 이용해서 N을 나눠본다. 만약에 나누어 떨어지면 N // K 값을 N에 갱신하고, count 값을 증가시킨다.  continue
# 나누어 떨어지지 않는다면, 나머지 값을 구하고 나머지 값을 count에 더해준다. 

N, K = map(int, sys.stdin.readline().split())

count = 0
while N > 1 : 
    result = N // K
    remain = N % K  
    
    if remain == 0 :
        count += 1 
        N = result
        continue

    count += remain
    N = N - remain

if N == 0 :
    count -= 1

print(count)