# Given an integer, n, print the following values for each integer i from 1 to n:
# 1) Decimal
# 2) Octal
# 3) Hexadecimal (capitalized)
# 4) Binary
# The four values must be printed on a single line in the order specified above for each i from 0 to n. 
# Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.
# Constraints
# 1 <= n <= 90

# Helper functions

def valid_input(num):
    if (num == 0) or (num > 90):
        return False
    else:
        return True

def print_formatted(num):
    width = len(bin(num)) - 2 # max width for the binary numbers
    for i in range(1, num+1):
        dec = str(i).rjust(width)  # Decimal
        octal = str(oct(i))[2:].rjust(width)  # Octal without prefix '0o'
        hexa = str(hex(i))[2:].upper().rjust(width)  # Hexadecimal without prefix '0x', en mayúsculas
        binary = str(bin(i))[2:].rjust(width)  # Binary without prefix '0b'
        print(dec, octal, hexa, binary)

    
if __name__ == '__main__':
    print("Enter an integer between 1 and 90")
    n = int(input())
    if valid_input(n) == False:
        print("Invalid input")
    else:
        print_formatted(n)
