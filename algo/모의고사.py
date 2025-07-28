# 그냥 각 리스트에 넣고, 하나 하나 돌리면 ?? 10,000 * 3번 아닌가 ? 

def solution(answers):
    
    math_quitter_one = [1,2,3,4,5]
    math_quitter_two = [2,1,2,3,2,4,2,5]
    math_quitter_three = [3,3,1,1,2,2,4,4,5,5]
    
    hit_count = [0, 0, 0]
    
    
    for answer_index in range(len(answers)) :
        
        submit_index = answer_index % len(math_quitter_one)
        if math_quitter_one[submit_index] == answers[answer_index] :
            hit_count[0] += 1
            
        submit_index = answer_index % len(math_quitter_two)
        if math_quitter_two[submit_index] == answers[answer_index] :
            hit_count[1] += 1
        
        submit_index = answer_index % len(math_quitter_three)
        if math_quitter_three[submit_index] == answers[answer_index] :
            hit_count[2] += 1
    
    max_count = max(hit_count)
    
    result = []
    for index in range(len(hit_count)) :
        if max_count == hit_count[index] :
            result.append(index + 1)
    
    return result