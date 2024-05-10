# REQUIREMENTS

# Input
# The first line contains a single string, s, with len(s) = n.
# The second line contains an integer, k, the length of each substring.

# Constraints
# 1 <= n <=10^4
# 1 <= k <= n
# n is a multiple of k

# We can split s in n/k substrings where each substring consists of the contiguous block of k characters in s.
# Any repeat occurrence of a character is removed from the string such that each character in the substrings occurs exactly once. 

# Output
# Print each subsequence on a new line. 
# There will be n/k of them. 
# No return value is expected.

# Example: 
# Input: s = 'AAABCADDE', k = 3
# The substrings of length 3 are: 'AAA', 'BCA' and 'DDE'. Since 2 of them have repeated characters, the output would be: 'A', 'BCA' and 'DE'. 

import collections

def valid_input(string, k):
    n = len(string)
    if n % k == 0 and string.isalpha():
        return True
    else:
        return False 

def remove_duplicates(string):
    unique_letters = set(string)
    sorted_letters = sorted(unique_letters, key=string.index)
    new_string = ''.join(sorted_letters)
    return new_string

def merge_the_tools(string, k):
    n = len(string)
    number_of_substrings = int(n/k)
    for i in range(number_of_substrings):
        substring = string[(k*i):(k*i+k)]
        print(remove_duplicates(substring))

if __name__ == '__main__':
    print("Enter a string and an integer that is a divisor of the length of the string")
    string, k = input(), int(input())
    if valid_input(string, k):
        merge_the_tools(string, k)
    else:
        print("Invalid set of inputs")

