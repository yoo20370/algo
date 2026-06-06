# 모든 경우의 수에 대해서 탐색하며 된다.
# bfs 혹은 재귀 함수를 이용해서 풀면 될 것 같다. 

count = 0 

def recusion(numbers, target, currentIndex, currentSum) :
    global count 
        
    # 인덱스를 넘어감 그러므로 종료해야 함 (종료 조건)
    if currentIndex >= len(numbers) :
        if currentSum == target :
            count += 1
        return 
    
    # 다음 재귀를 수행해야함 
    # 현재 인덱스에서 가능한 경우의 수 + 1 or -1
    recusion(numbers, target, currentIndex + 1, currentSum + numbers[currentIndex])
    recusion(numbers, target, currentIndex + 1, currentSum - numbers[currentIndex])
    

def solution(numbers, target):
    
    recusion(numbers, target, 0, 0)
    
    return count