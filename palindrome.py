# input : KayaK
# output : true

str = 'KayaK'

def is_palindrome(str, s, e):
    if s < 0 or e > len(str) or s > e:
        return False

    if s == e:
        return True 
    
    if not str[s] == str[e]:
        return False

    
    return is_palindrome(str, s + 1, e - 1)


print(is_palindrome(str, 0, len(str) - 1))