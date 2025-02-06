import sys

N, K = map(int, sys.stdin.readline().split())

# N + 1 크기의 리스트를 생성해서 True으로 초기화해준다. 
# 2부터 int(N ** 0.5) 수의 배수를 제거한다. (소수가 아닌 수는 a * b 형태이기 때문에)
# 제거할 때, 순서를 카운트한 후 K 번째인지 확인하여 K번째면 현재 삭제된 값을 반환한다. 

prime_array = [True] * (N + 1) 

count = 0

result = 0
for i in range(2, N + 1) :

    if prime_array[i] == True :

        j = 1
        while i * j <= N :
            if prime_array[i * j] == True :
                prime_array[i * j] = False
                count += 1
                if count == K :
                    result = i * j
            j += 1

print(result)
