# 6 5 3 1 0

# 6을 보고 앞에 6개인 것이 있나 확인
# 5
# 4
# 3 내려가면서 몇개 있나 확인함 -> 3개 이상인데 몇 개인지 확인할 수 있게 됨 

# 오름차순 정렬하면, 현재 값보다는 큰 값이 앞에 존재한다. 하지만 앞의 값이 본인과 동일한지 큰지 알 수 없음(얼마나 큰지 알 수 없음) 
# 큰 값이 있는 것을 확인해야 함 -> 어떻게 확인할건데 ?? 
# 3 3 3 3 3

# 6 5 5 5 -> 개수랑 마지막으로 만난 최대값의 크기를 가지고 있으면 ?

# 현재 값이 현재 개수보다 크다면, -> 현재 값이 최대값 
def solution(citations):
    citations.sort(reverse=True)
    
    h = 0 
    cnt = 0
    for curr_value in citations :
        if curr_value <= cnt :
            return cnt 
        cnt += 1
    
    return cnt