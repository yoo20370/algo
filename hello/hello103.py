def solution(number, k):
    
    length = len(number)
    
    numberList = [int(i) for i in number]
    
    stack = [numberList[0]]
    
    index = 1
    
    for index in range(1, length) :
        while stack and stack[-1] < numberList[index] and k > 0:
            stack.pop()
            k -= 1
            
        stack.append(numberList[index])
            
    while k > 0 :
        stack.pop()
        k -= 1
        
    answer = ''
    for number in stack :
        answer += str(number)
    
    return answer