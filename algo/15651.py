import sys 

def dfs(length, result, N, M) :


    if length == M :
        for number in result :
            print(number + 1, end=" ")
        print()
        return 
    
    for index in range(N) :
        if not result or (result and result[-1] <= index) :
            result.append(index)
            dfs(length + 1, result, N, M)
            result.pop()

def solution() :
    N, M = map(int, sys.stdin.readline().split())


    dfs(0, [], N, M)
solution()