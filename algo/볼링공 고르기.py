import sys, itertools

# 1 3 2 3 2 

# 1 -> 4개
# 3 -> 2개
# 2 -> 1개
# 3 -> 1개 


# 0 1 2 3 4 5 6 7 8 9 10
# 0 0 1 0 0 0 0 0 0 0 0 
# 1 -> 2 + 2 -> 4개
# 3 -> 2 -> 2 개 
# 2 -> 1 -> 1개
# 3 -> 1 -> 1개

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




