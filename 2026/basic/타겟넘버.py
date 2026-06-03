count = 0 

def recusionFunc(numbers, target, sum, index) :
    global count
    
    if index == len(numbers) :
        if target == sum :
            count += 1
        return 
    
    result = sum + numbers[index]
    recusionFunc(numbers, target, result, index + 1)
        
    result = sum - numbers[index]
    recusionFunc(numbers, target, result , index + 1)
    

def solution(numbers, target):
    
    recusionFunc(numbers, target, 0, 0)
    
    return count