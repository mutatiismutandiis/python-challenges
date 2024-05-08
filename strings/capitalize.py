# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# Given a full name, your task is to capitalize the name appropriately.

# Input Format
# A single line of input containing the full name: s

# Constraints
# 0 < len(s) <1000
# The string consists of alphanumeric characters and spaces.

#Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

# Herlper function
def solve(s):
    capitalized_name = ''
    list = s.split(' ')
    for name in list:
        capitalized_name = capitalized_name + name.capitalize() + ' '
    return capitalized_name
    
if __name__ == '__main__':
    print("Enter your full name")
    s = input()
    result = solve(s)
    print(result)
   

