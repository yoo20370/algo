import sys, itertools

# 내 생각
# 일단 테이블에 개수 기록한다.
# 본인 테이블를 제외한 나머지의 합을 카운트한다.
# 본인 테이블의 개수를 1 내린다. -> 빼주지 않으면 나중에 다른 테이블 구할 때 중복 계산 됨 0, 1 -> 1, 0 (여기서 0과 1은 인덱스)

def solution() :
    N, M = map(int, sys.stdin.readline().split())

    table = [0 for i in range(M+1)]

    ball_list = list(map(int, sys.stdin.readline().split()))
    for curr in  ball_list:
        table[curr] += 1 

    count = 0 

    for curr_ball in ball_list :
        count += sum(table) - table[curr_ball]
        table[curr_ball] -= 1

    return count
print(solution())




