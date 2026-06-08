# 주식 가격

# 초 단위로 기록된 주식 가격임 
# 가격이 떨어지지 않은 기간을 구해야 함 
# 첫 가격보다 떨어지는 구간을 구해야 함 -> 
# 왼쪽에서 오른쪽으로 순회해서 낮아지는 구간을 구해야함 -> O(N**2) 임
# 결국 왼쪽에서 오른쪽으로 순회하는 횟수를 줄여야 함 
## 첫 번째 가격은 두 번째 가격이 떨어졌을 때만 떨어질 가능성이 있음 
## 두 번째 가격 보다 크면 첫 번째 가격은 무조건 떨어지지 않음 
## 현재 가격이 오른쪽 가격과 비교했을 때, 오른쪽 가격이 크다면 현재 가격은 스택에 넣는다.
## 현재 가격 보다 더 작다면, 떨어진 위치를 기록하고, 스택에서 꺼내어 확인한다. 
## prices는 큐에 넣고 앞에서부터 차근차근 꺼낸다. 

from collections import deque

def solution(prices):
    
    length = len(prices)
    
    answer = [0] * length 
    
    stack = []
    
    prices = deque(prices)
    
    while prices :
        currentPrice = prices.popleft()
        currentIndex = length - len(prices) - 1 # 이미 꺼냈기 때문에 인덱스는 - 1 을 해줘야 함
        
        # 다음 가격이 현재 가격보다 가격이 떨어졌다면 (>), 기록해야함 
        # 떨어지지 않은 기간 = 떨어진 위치 - 본인 위치 
        if prices and currentPrice > prices[0] :
            answer[currentIndex] = length - len(prices) - currentIndex
            
            while stack and stack[-1][0] > prices[0] :
                currentPrice, currentIndex = stack.pop()
                answer[currentIndex] = length - len(prices) - currentIndex
            
        else :
            stack.append([currentPrice, currentIndex])
    
    
    while stack :
        currentPrice, currentIndex = stack.pop()
        answer[currentIndex] = length - 1 - currentIndex
        
    
    return answer