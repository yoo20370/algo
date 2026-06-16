## 같은 숫자는 싫어

# 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거한다. 
# 그럼 결국 앞에서 시작해서 다음 인덱스를 비교해가며, 연속적인 숫자가 등장할 때 같은 숫자인 경우는 answer에 삽입하지 말고
# 같은 숫자가 아닌 경우는 연속적인 숫자이므로 answer에 넣는 방식으로 가야할 것 같음  

def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    # 마지막 인덱스는 접근할 이유가 없음 
    for index in range(len(arr) - 1) :
        if arr[index] != arr[index + 1] :
            answer.append(arr[index + 1])
    
    return answer
        