# 더하거나 뺴거나
# bfs

# 더하거나 빼거나 
# bfs 풀이 

def solution(numbers, target):
    
    answer = 0
    
    # 스택에 무엇을 넣을건가요 ?? 
    # (현재 인덱스, 현재 합)
    stack = []
    
    stack.append((0,0))
    
    while stack :
        currentIndex, currentSum = stack.pop()
        
        # 각 인덱스의 경우의 수 2가지 
        if currentIndex < len(numbers) :
            stack.append((currentIndex + 1, currentSum + numbers[currentIndex]))
            stack.append((currentIndex + 1, currentSum - numbers[currentIndex]))
        
        else :
            # 결국 인덱스를 넘어갔다면 target 값과 같은지 비교 
            if currentSum == target :
                answer += 1  
                
    return answer