from operator import countOf
import os

max_strikes = 10
win_if_true = True

letter_bank = [chr(ord('a') + x) for x in range(26)]  # list of all 26 valid letters, lowercase only
letters_not_found = []  # will hold all letters guessed but not present in the secret string

secret_string = input("Enter the secret word or phrase: ").lower()  # inputs the secret string
os.system('cls||clear')  # Clear the screen to hide the secret

secret = list(secret_string)  # divides secret_string into a list of letters

# Create the initial display.  This is a copy of secret where all the letters 
# have been turned to underscores, but punctuation is passed through unchanged.
# There are 2 ways to do this: for loop and list comprehension.
# Each of the following have the same result:
## FOR LOOP
display = []
for x in secret:
    if x.lower() in letter_bank:
        display.append("_")
    else:
        display.append(x)
## LIST COMPREHENSION
display = ["_" if x.lower() in letter_bank else x for x in secret]



# While puzzle is not solved
while "_" in display: # <-- add the correct condition
    print ("*************************")
    print(*display)  # Prints the current display of the puzzle.  * operator unpacks a list into arguments. 
    print("*************************")
    # Print the list of letters not found, if there are any
    if len(letters_not_found) != 0:
        print("Letters not found: ", *letters_not_found)
    # Gather input until valid.  Use while True ... if break structure.
    while True:
        # input a letter
        letter = input("Choose a letter: ").lower()
        # Check for validity and if the letter was already tried
        if len(letter) != 1:
            print("Please only guess 1 character")
        elif not letter.isalpha():
            print ("Please only use alphabet characters")
        elif letter in letters_not_found:
            print("letter was already tried")
        else:
            break

    # Count how many times it appears in secret and change display 
    # from underscore to the correct letter in those spots
    # Use a for loop or list comprehension to change display.
    if letter in secret:
        for x in range(len(secret)):
            if letter.lower() == secret[x]:
                display.pop(x)
                display.insert(x, letter)
        
    # Say if found or not found
    # if the letter is found in secret, say how many instances found
    if letter in secret:
        print(f"There was {countOf(secret, letter)} in the word")
    # if not found, add to list of letters not found
    else:
        letters_not_found.append(letter)
        
    # if too many strikes (len of letters_not_found), end the game
    if len(letters_not_found) >= max_strikes:
        win_if_true = False
        break
        
# Print the display one more and the list of letters not found, 
# if any, same as at the beginning of the while loop.
print (*display)
if len(letters_not_found) != 0:
        print("Letters not found: ", *letters_not_found)
# Display messages for winning and losing, as appropriate
if win_if_true:
    print("You win!")
else:
    print ("You lose!")
print(f"\"{secret_string}\"")  # reveals the secret string
