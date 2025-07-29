
import sys 

def dfs(start_computer, visited, computers, n) :
    visited.add(start_computer)
    
    for col in range(n) :
        if col not in visited and computers[start_computer][col] == 1 :
            dfs(col, visited, computers, n)
        
def solution(n, computers):
    
    visited = set()
    
    count = 0
    for row in range(n) :
        if row not in visited :
            count += 1
            dfs(row, visited, computers, n)
    
    return count