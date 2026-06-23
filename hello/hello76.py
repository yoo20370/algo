# 기능 개발
# 각 기능은 진도가 100일 때 서비스에 반영 가능 
# 뒤에 기능이 앞의 기능보다 먼저 개발될 수 있음
# 앞에 있는 기능이 배포될 때 함께 배포 

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
# 각 작업의 개발 속도가 적힌 배열 speeds가 주어짐

# 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 하라 

# 현재 배포를 기준으로 며칠 걸리는지 계산
# 그리고 현재 배포 이후의 배포를 순회하면서 해당 기간 동안 이미 기능이 완성된 녀석을 구하면 됨 
import math 
from collections import deque 

def solution(progresses, speeds):
    
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses :
        currentProgress = progresses.popleft()
        currentSpeed = speeds.popleft()
        
        remainPercent = 100 - currentProgress
        
        requiredDayForDeploy = int(math.ceil(remainPercent / currentSpeed))
        
        # 현재 배포 포함시켜야 함 
        count = 1
        while progresses : 
            nextProgress = progresses[0]
            nextSpeed = speeds[0]
            
            remainPercent = 100 - nextProgress
            
            if remainPercent <= nextSpeed * requiredDayForDeploy :
                # 배포할 때 같이 배포 가능 
                count += 1
                progresses.popleft()
                speeds.popleft()
            else : 
                # 배포 할 떄까지 배포할 수 없는 상태 
                break
        
        answer.append(count)
        
        
    return answer