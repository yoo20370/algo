# 기본 순회의 경우 O(N)
# 이진 탐색의 경우 O(NlgN) -> 정렬 비용 때문 
# Set의 경우 O(N) 배열을 순회해서 Set으로 만들어야 함 

# 만약 여기서 값이 무수히 많고, 하나의 배열에 대해서 여러 번 사용되는 경우 -> 이진 탐색 활용  
# 값이 많지만 Set()에서 해시 테이블이 감당 가능한 수준이고, 하나의 배열에 대해서 여러 번 사용 되는 경우 -> Set() 사용 
# 배열을 한 번, 원소 한 번 찾기 -> 그냥 순회 

# 이유 -> 이미 리스트로 값이 들어왔기 때문 
# 받는 상황이라면 처음부터 set()으로 받으면 더 효율적일 수 있음
# 다만 이미 리스트로 값이 존재하고 이를 Set()으로 변환하려면 기본적으로 리스트를 순회해야 함 
# 그러므로 위와 같은 판단을 내렸음 

# Set을 사용했지만 여러 번 사용할 수 없다는 점 ..... 인지해야 함 
# 입력 자체가 set이 아니라 배열로 들어오기 때문 
def is_number_exist(number, array):
    
    arraySet = set(array)

    if number in arraySet :
        return True 
    else :
        return False

result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))