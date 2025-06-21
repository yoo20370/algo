# 문제를 제대로 읽어야 한다. -> 솔직히 그림 보고 낚임 
# 여기서 각 배열은 가로로 나열되어 있다. 

def solution(board, moves):
    
    stack = []
    answer = 0
    
    for move in moves :
        
        index = move - 1
        for curr_board in board :
            if curr_board[index] != 0 :
                select_board = curr_board[index]
                curr_board[index] = 0
                
                if stack and stack[-1] == select_board :
                    stack.pop()
                    answer += 2 
                else :
                    stack.append(select_board)
                break
            
    return answer