# Requirements:
# Mat size must be NxM (N is an odd natural number, and M is 3 times N)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

# Constrains:
# 5 < N < 101
# 15 < M < 303

def valid_input(value):
    if (value%2 == 1) and (5 < value < 101):
        return True
    else:
        return False

def upper_triangle(value):
    rows = int(value/2)
    width = value * 3
    for i in range(1, rows+1):
        bars = i * 2 - 1
        dots = (width - bars * 3) // 2
        # Generate triangle row
        row = '-' * dots + '.|.' * bars + '-' * dots
        print(row)

def welcome(value):
    welcome = 'WELCOME'
    bars = int((value * 3 - len(welcome))/2)
    # Generate WELCOME row
    row = '-' * bars + welcome + '-' * bars
    print(row)

def inverted_triangle(value):
    rows = int(value/2)
    width = value * 3
    for i in range(rows, 0, -1):
        bars = i * 2 - 1
        dots = (width - bars * 3) // 2
        # Generate triangle row
        row = '-' * dots + '.|.' * bars + '-' * dots
        print(row)        

def door_mat_generator(value):
    upper_triangle(value)
    welcome(value)
    inverted_triangle(value)


if __name__ == '__main__':
    print("Enter and odd integer number between 5 and 101:")
    num = int(input())
    if (valid_input(num) == True):
        door_mat_generator(num)
    else:
        print("Invalid input")
