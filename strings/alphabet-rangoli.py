# You are given an integer, N. 
# Your task is to print an alphabet rangoli of size #. 
# (Rangoli is a form of Indian folk art based on creation of patterns)

# Example:
# size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

#The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

# Input
# int size: the size of the rangoli

# Output
# A single string made up of each of the lines of the rangoli separated by a newline character (\n)

# Constraints
# 0 < size < 27

# Helper funcions

def valid_input(num):
    if (0<num<27):
        return True
    else:
        return False

def generate_triangle(num):
    lines = []
    for i in range(0, num-1):
        row = '-'*(2*(num-(i+1))) + generate_middle_string(num, i) + '-'*(2*(num-(i+1)))
        lines.append(row)
    return lines


def generate_triangle_down(num):
    lines = []
    for i in range(num - 1, 0, -1):
        row = '-'*(2*(num-i)) + generate_middle_string(num, i - 1) + '-'*(2*(num-i))
        lines.append(row)
    return lines

def generate_middle_string(num, line):
    line_chars = [chr(96 + num - j) for j in range(line, -1, -1)]
    return '-'.join(line_chars[::-1] + line_chars[1:])
    
    
def generate_center_line(num):
    center_line = ''
    # First half: from the size down by one we add the char and a -, unless is the last one, then only the char
    for i in range(num, 0, -1):
        center_line += chr(96 + i) + '-' if i != 1 else chr(96 + i)
    # Second half: from 2 to size we add the char and the -, unless is the last one
    for i in range(2, num + 1):
        center_line += '-' + chr(96 + i) if i != num else '-' + chr(96 + i)
    return center_line
        
def print_rangoli(size):
    triangle_up = generate_triangle(size)
    center_line = generate_center_line(size)
    triangle_down = generate_triangle_down(size)

    result = triangle_up + [center_line] + triangle_down
    print('\n'.join(result))
    
if __name__ == '__main__':
    print("Enter a size for your Rangoli between 0 and 27")
    n = int(input())
    if valid_input(n) == False:
        print("Invalid input")
    else:
        print_rangoli(n)