import textwrap

# Constraints
# 0 < len(string) <1000
# 0 <max_width < len(string)

# Helper function
def wrap(string, max_width):
    wrapped_text = textwrap.fill(string, max_width)
    return wrapped_text

# Input and Output
if __name__ == '__main__':
    print("Enter a long string with less than 1000 characters:")
    string = input()
    if ((len(string) == 0) or (len(string)>=1000)):
        print("Invalid input: 0 < len(string) <1000")
    else:
        print("Enter the width you want to wrap the text to:")
        max_width = int(input())
        if (max_width<=0 or max_width>=len(string)):
            print("Invalid input: The length to wrap the text with should be greater than zero and smaller than the string length")
        else:
            result = wrap(string, max_width)
            print(result)