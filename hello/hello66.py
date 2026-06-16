# K번째 수 

# command의 2차원 배열 개수 만큼 결과가 나온다.
# 각 2차원 배열을 순회하면서 
# firstIndex - 1 <= list  <= secondNumber 를 구하면 될 것 같음 

def getKNumber(first, second, third, array) :
    
    # first - 1인 이유는 첫 번째 숫자는 인덱스 0에 해당
    # second는 그냥 사용하는 이유는 애초에 인덱스이므로 -1 이지만 결국 second에 해당하는 값도 리스트에 포함되어야 하기 때문
    currentList = array[first-1:second]
    
    sortedList = sorted(currentList)

    return sortedList[third - 1]
    
def solution(array, commands):
    
    answer = []
    for index in range(len(commands)) :
        first, second, third = commands[index]
        result = getKNumber(first, second, third, array)
        answer.append(result)
    
    return answer