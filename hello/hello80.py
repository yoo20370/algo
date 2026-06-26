def solution(phone_book):
    phone_book_set = set(phone_book)
    
    for phone in phone_book :
        for index in range(len(phone) - 1) :
            prefix = phone[:1 + index]
            
            if prefix in phone_book_set :
                return False 
    answer = True
    return answer
