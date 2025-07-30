import sys

# dfs, 백트래킹으로 풀어보자 
# 순회하면서 방문하고, 방문 처리 

def dfs(curr_length, result, N, M) :

    if curr_length == M :
        for number in result :
            print(number + 1, end=" ")
        print()
        return 
    
    for index in range(N) :
        if index not in result :
            result.append(index)
            dfs(curr_length + 1, result, N, M)
            result.pop()
            
def solution() :
    N, M = map(int,sys.stdin.readline().split())

    dfs(0, [] ,N, M)
    

solution()