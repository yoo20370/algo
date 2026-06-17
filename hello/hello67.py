# 최소 직사각형 

def solution(sizes):
    
    row, col = sizes[0]
    
    maxSize = max(row, col)
    minSize = min(row, col)
    
    for index in range(1, len(sizes)) :
        currentRow, currentCol = sizes[index]
        
        currentMax = max(currentRow, currentCol) 
        currentMin = min(currentRow, currentCol)
        
        if currentMax > maxSize :
            maxSize = currentMax
        
        if currentMin > minSize :
            minSize = currentMin
            
    return maxSize * minSize
    
