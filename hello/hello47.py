# 탑 
# 마지막 탑부터 오른쪽에서 왼쪽으로 신호를 발사
# 만약 발사한 신호가 탑 수신기에 닿는다면 이를 기록하라
# 가장 쉬운 방법은 N번째 탑은 최대 N-1 탑을 검사해서 수신하는 탑이 있는지 확인하면 됨 
# 다만 탑의 개수가 무수히 많은 경우 시간 복잡도 O(N**2)라서 정해진 시간에 처리하지 못할 수 있음
# 
# 신호가 닿는 탑을 검사하는 시간을 줄여야 함 
# 바로 옆 탑으로 신호를 쐈을 때, 닿지 않았다면, 현재 탑은 건너뛰고, 옆의 탑이 바로 옆 탑에 닿는지 확인한다. (스택에 저장 )
# 마찬가지고 닿지 않았다면, 현재 탑은 건너뛴다. -> 즉, 이전 탑에서 현재 탑에 신호를 보내지 못했으므로 더 작은 탑에서 닿지 못한 신호라면 똑같이 닿지 못할 것 
# 만약 닿았다면 신호가 닿은 위치를 기록하고, 닿지 않을 때까지 스택에서 탑을 꺼내서 시도한다. 


top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):

    length = len(heights)

    # 신호가 도달하지 못한 경우는 모두 0이기 때문 
    answer = [0] * length

    stack = []

    while heights :
        currentHeight = heights.pop()
        currentIndex = len(heights) # 말 그대로 인덱스임 위치는 1을 더한 값 

        if heights and currentHeight <= heights[-1] :
            answer[currentIndex] = len(heights)

            while stack and stack[-1][0] <= heights[-1] :
                topHeight, topIndex = stack.pop()
                answer[topIndex] = len(heights)

        else :
            stack.append((currentHeight, currentIndex))
    

    return answer
    
    
print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 2, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))