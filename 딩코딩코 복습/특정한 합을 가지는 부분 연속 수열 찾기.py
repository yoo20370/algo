n = 5 
array = [1, 2, 3, 2, 5]
target = 5 



start = 0
end = 0

# 어떻게 풀어야 할 까
# 타겟보다 값이 작다면 end 포인터를 앞으로 이동
# 타겟보다 값이 크다면 start 포인터를 앞으로 이동 
# 포인터가 같은 값을 가리키는 경우 한 원소와 값을 비교 
# 연속 수열의 합이 target보다 커질 때까지 start 포인터를 앞으로 이동
# 작거나 같다면 end 포인터 이동 
# 이 떄 같으면 count를 세준다. 
count = 0

curr_sum = array[start]
while True :
    while curr_sum < target and start < end :
        start += 1
        curr_sum = array[start] + array[end]
    
    if target == curr_sum :
        count += 1
    


    
    



