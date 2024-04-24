def is_any_alnum(value):
    for char in value:
        if char.isalnum():
            return True
    return False
    
def is_any_alpha(value):
    for char in value:
        if char.isalpha():
            return True
    return False
    
def is_any_digit(value):
    for char in value:
        if char.isdigit():
            return True
    return False

def is_any_lower(value):
    for char in value:
        if char.islower():
            return True
    return False
    
def is_any_upper(value):
    for char in value:
        if char.isupper():
            return True
    return False
    
if __name__ == '__main__':
    print("Enter a string:")
    s = input()
    N = len(s)
    
    print(is_any_alnum(s))
    print(is_any_alpha(s))
    print(is_any_digit(s))
    print(is_any_lower(s))
    print(is_any_upper(s))
