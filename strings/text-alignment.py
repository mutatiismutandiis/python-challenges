# INPUT: A single line containing the thickness value for the logo: odd integer between 0 and 50
# OUTPUT: H logo with the right size

# Helper function
def is_valid_input(value):
    if (N<=0 or N>=50):
        print("0<thickness<50")
    elif (value%2 == 0):
        print("Thickness needs to ve an odd number")
    else:
        return True

# Helper functions to generate all the shapes according to the size
def triangle_up(size):
    s = "H"
    line_length = 2*size - 1
    for i in range(size):
        string_to_show = s.center(line_length)
        print(string_to_show)
        s = s+"HH"


def equal_columns(size):
    
    initial_space = " " * int((size-1)/2)
    column = "H" * size
    space_in_between = " " * (3*size)
    string_to_show = initial_space + column + space_in_between + column
    
    for i in range(size+1):
        print(string_to_show)
 
    
def center_line(size):
    
    starting_space_length = int((size-1)/2)
    starting_space = " " * starting_space_length
    
    s = "H" * (5*size)      
    string_to_show = (starting_space + s).ljust(5*size)
    amount_of_lines = int((size+1)/2)
    
    for i in range(amount_of_lines):
        print(string_to_show)


def triangle_down(size):
    line_length = int(6*size-1)
    s = "H" * (2*size - 1)
    
    for i in range(size):
        string_to_show = s.rjust(line_length)
        print(string_to_show)
        s = s[2:] + " "

# Input and Output
print("Enter a thickness for the logo between 0 and 50:")
N = int(input())

if (is_valid_input(N) == True):
    triangle_up(N)
    equal_columns(N)
    center_line(N)
    equal_columns(N)
    triangle_down(N)