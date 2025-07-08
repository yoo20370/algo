
def possible(answer) :
    
    for x, y, object in answer :
        if object == 0 : # 기둥인 경우 
            if y == 0 or [x, y-1, 0] in answer or [x, y, 1] in answer or [x - 1, y, 1] in answer :
                continue
            return False 
        
        elif object == 1 :
            # 보인 경우 
            if [x, y-1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer) :
                continue
                
            return False
        
    return True 
def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, object, command = frame
        if command == 0 :
            answer.remove([x, y, object])
            if not possible(answer) :
                answer.append([x, y, object])
        if command == 1 :
            answer.append([x, y, object])
            if not possible(answer) :
                answer.remove([x, y, object])
        
    answer.sort()
    return answer