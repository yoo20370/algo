# 주식 가격 

# 초 단위로 주식 가격이 변함 
# 내 주식 가격이 떨어지는 지점을 찾아야 함 
# 간단하게 풀면 앞에서 부터 하나하나 확인해야 함 O(N**2) -> 입력값이 10만개인 경우 시간 복잡도가 너무 큼 
# 하나하나 비교하는 것을 줄여야 할 것 같음 -> 
# 주식 바로 다음 가격에 대해서 같거나 올라갈수도, 떨어질 수도 있음 
# 만약 다음 가격이 올랐다고 가정했을 때, 현재 주식 가격이 떨어지지 않았음 
# 다음 가격에 대해서 다음 가격이 올랐다면 ?? 현재 주식 가격도 떨어지지 않음 
# 반대로 다음 가격에 대해서 다음 가격이 떨어졌다면 ?? 현재 주식 가격도 떨어졌을 가능성이 있음 
## 이를 활용해야 할 것 같음 
## 만약 바로 옆 주식 가격이 떨어졌다면, 바로 기록한다.
## 가격이 같거나 올랐다면, 스택에 넣는다. 
## 만약 스택이 비어있지 않을때 바로 주식 가격이 떨어졌다면, 스택에서 주식을 꺼내서 가격을 비교해야 함 

### 착각한게 떨어진 위치를 계산을 해야함.... 
## 그걸 구해보자 
def solution(prices):
    
    length = len(prices)
    
    # 마지막 원소의 경우 비교할 대상도 없으므로 0으로 기록해야 해서 0으로 초기화 
    answer = [0] * (length)
    
    stack = []
    
    index = 0 
    # 현재 인덱스와 다음 인덱스를 비교할 것이기 때문 
    # 해당 반복문은 바로 옆 인덱스 가격과 비교할 것임 -> index + 1 값이 length 값과 같다면 list 범위를 넘어선다. 
    while index + 1 < length : 
        
        # 바로 주식이 가격이 떨어진 경우 
        if prices[index] > prices[index + 1] :
            # 기록해야 하는 위치값이 index + 1 이기 때문 
            answer[index] = index - index + 1
        
            # 만약 스택에서 꺼낸 값도 떨어졌다면, 확인한다.
            # 만약 스택 Top에 있는 값이 크거나 같다면, 반복문을 멈춘다. 
            while stack and stack[-1][1] > prices[index + 1] :
                currentIndex, currentPrice = stack.pop()
                answer[currentIndex] = index - currentIndex + 1
        else : 
            stack.append((index, prices[index]))
        # 다음 인덱스로 이동 
        index += 1
    
    # 끝까지 안 떨어졌으므로 안 떨어진 위치를 기록해야 함 
    while stack :
        currentIndex, currentPrice = stack.pop()
        answer[currentIndex] = length - currentIndex - 1
    
    return answer