
def solution(n, times):
    
    maxTime = max(times)
    
    pl = 1
    pr = n * maxTime
    
    answer = pr
    while pl <= pr :
        currentTime = (pl + pr) // 2
        
        totalPass = 0
        for time in times :
            totalPass += currentTime // time
        
        if totalPass < n :
            pl = currentTime + 1
            
        elif totalPass >= n :
            pr = currentTime - 1
            answer = currentTime
        
    return answer
        
            
            