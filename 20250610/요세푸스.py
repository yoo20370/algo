# BOJ 1158

# 어떻게 풀 것인가 
# 우선 배열에 값을 순서대로 저장 
# 첫 번째 꺼낼 인덱스는 k - 1로 설정 
# 다음 꺼낼 인덱스는 + 2 -> 이전 데이터가 뽑혀서 한 칸씩 앞 당겨지기 때문
# 만약 인덱스 범위를 벗어나면 테이블 크기로 나눈다. (반복)

def josephus_problem(n, k):
    group = [i for i in range(1, n + 1)]
    result = []

    # 첫 번째 인덱스 계산 
    target_index = k-1 
    while len(group) != 1 :
        result.append(group.pop(target_index))
        target_index += k-1

        while len(group) <= target_index:
            target_index = target_index % len(group)
    result.append(group.pop())
    
    # join의 구분자는 마지막 요소 뒤에 붙지 않는다.
    print("<", ", ".join(map(str, result)), ">", sep="")

n, k = map(int, input().split())
josephus_problem(n, k)


