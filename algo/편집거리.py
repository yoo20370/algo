# 편집 거리 알고리즘으로 풀어야 함 -> BFS로 덤볐다가 index out of range와 무지막지한 연산으로 인해 풀지 못함 ㅠㅠ 
# 2차원 memo[i][j]에 들어가는 값은 a[:i], b[:j] 일 때 a를 b로 만들 때 몇 번의 최소 편집을 수행해야하는지 

import sys 

def solution() :

    string_a = sys.stdin.readline().rstrip()
    string_b = sys.stdin.readline().rstrip()

    a_length = len(string_a)
    b_length = len(string_b)

    memo = [[0] * (b_length + 1) for _ in range(a_length + 1)]

    for i in range(1, a_length + 1) :
        memo[i][0] = i

    for j in range(1, b_length + 1) :
        memo[0][j] = j

    
    for i in range(1, a_length + 1) :
        for j in range(1, b_length + 1) :
            if string_a[i - 1] == string_b[j - 1] :
                memo[i][j] = memo[i-1][j-1]
            else :
                memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
    
    print(memo[a_length][b_length])

solution()