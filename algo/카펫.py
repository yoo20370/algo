# 어떻게 풀어야 하지 ?? 
# 노란색을 어떻게 배치하느냐에 따라 브라운색 개수가 달라짐 
# 가로 세로 길이라는 거 보니까 노란색은 정사각형 혹은 직사각형이 되어야 함 
# 24의 약수를 구하고 노란색 사각형에 따른 브라운 개수를 구한다.
# 브라운 개수를 구하는 방법은 따로 함수로 만든다. 

def getDevisorsFor(number) :
    
    result = set()
    for i in range(1, int(number ** (0.5)) + 1) :
        if number % i == 0 :
            result.add(i)
    return sorted(result)

def getBrwonCountFor(yellowRow, yellowCol, yellowCount) :
    return (yellowRow + 2) * (yellowCol + 2) - yellowCount 

def solution(brown, yellow):
    
    divisors = getDevisorsFor(yellow) 
    
    for index in range(len(divisors)) :
        
        col = divisors[index] 
        row = yellow // col 
        
        brown_count = getBrwonCountFor(row, col, yellow)
        
        if brown_count == brown :
            return max(row,col) + 2, min(row,col) + 2
    
    return 0

