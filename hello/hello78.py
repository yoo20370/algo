# 순열로 모든 경우를 구하고 최대값을 찾는 건 시간복잡도 때문에 안 됨 1000!lg1000! 말도 안 됨 

# 일단 모든 원소를 순회해서 맨 앞자리를 기준으로 dict에 저장할 거임 
# 그리고 각 dict 원소에 대해서 한 번 더 정렬할 거임 -> 여기서는 비교해서 정렬하는 방식으로 할 거임 

# 첫 번째 풀이
from functools import cmp_to_key

def compare(a, b) :
    
    AB = a + b
    BA = b + a
    
    if int(AB) < int(BA) :
        return 1
    elif int(AB) > int(BA) :
        return -1
    else :
        return 0 

def solution(numbers):
    
    dict = {}    
    for i in range(0, 10) :
        dict[i] = []
    
    for number in numbers :
        string = str(number)
        firstNumber = int(string[0])
        
        dict[firstNumber].append(string)
    
    for number in range(0, 10) :
        array = dict[number]
    
        array.sort(key=cmp_to_key(compare))

    result = ""
    for number in range(9, -1, -1) :
        
        array = dict[number]
        
        for string in array :
            result += string
    
    if len(numbers) == len(dict[0]) :
        return "0"
    
    return result

## 두 번째 풀이
from functools import cmp_to_key

def compare(a, b) :
    a = str(a)
    b = str(b)
    
    if a + b < b + a :
        return 1
    elif a + b > b + a :
        return -1
    else : 
        return 0 

def solution(numbers):
    
    numbers.sort(key=cmp_to_key(compare))
    
    result = ""
    
    for number in numbers :
        result += str(number)
        
    if sum(numbers) == 0 :
        return "0"
    
    return result