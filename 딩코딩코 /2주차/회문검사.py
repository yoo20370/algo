input = "우영우"

def is_palindrome(string):

    pl = 0
    pr = len(string) - 1

    while pl < pr :
        if string[pl] != string[pr] :
            return False
        
        pl += 1
        pr -= 1
    return True


print(is_palindrome(input))

input = "우영우"

def is_palindrome(string):
    if len(string) <= 1 :
        return True
    
    if string[0] != string[-1] :
        return False
    
    return is_palindrome(string[1:-1])


print(is_palindrome(input))