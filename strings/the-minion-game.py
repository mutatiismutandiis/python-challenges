# Game Rules
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# One player has to make words starting with consonants.
# The other player has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# Input Format
# A single line of input containing the string S.
# Note: The string S will contain only uppercase letters: A-Z.

# Constraints
# 0 <= len(S) <=10^6

# Output
# A single line with the winner's name and score, separated by a space on one line or 'Draw' if there is no winner

# Helper functions

def valid_input(string):
    return string.isalpha()

def minion_game(string):
    vowels = 'AEIOU'
    count_player_1 = 0
    count_player_2 = 0
    length = len(string)
    
    # Counting substrings
    for i in range(length):
        if string[i] in vowels:
            count_player_2 += length - i
        else:
            count_player_1 += length - i

    # Printing results
    if count_player_1 > count_player_2:
        print("Winner is player 1: ", count_player_1)
    elif count_player_2 > count_player_1:
        print("Winner is player 2: ", count_player_2)
    else:
        print("Draw")

if __name__ == '__main__':
    print("Enter a word")
    s = input().upper()
    if valid_input(s) == True:
        minion_game(s)
    else:
        print("Invalid input")