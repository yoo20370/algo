input = "abba"

def is_palindrome(string) -> bool :
    if len(string) <= 1 :
        return True
    
    if string[0] == string[-1] :
        return is_palindrome(string[1:-1])          
    else :
        return False

print(is_palindrome(input))