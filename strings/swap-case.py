# RequirementsÑ
# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters and vice versa.

# Constraints
# 0 < len(s) <= 100

# Helper function
def swap_case(s):
    alterned_string = ''
    for char in s:
        if char.islower():
            alterned_string = alterned_string + char.upper()
        else:
            alterned_string = alterned_string + char.lower()      
    return alterned_string


if __name__ == '__main__':
    print("Enter a valid string")
    s = input()
    result = swap_case(s)
    print(result)


