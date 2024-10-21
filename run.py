
import random

def display_instructions():
    """
    Instructions for the game read in from the
    instructions file and displayed.
    """  
    file = open("instructions.txt", 'r')
    instructions = file.read()
    print(instructions)
    file.close()

def choose_random_word():
    """
    Read in words from words file and assign to a 
    list using the new line as split. Randomly select
    a word from this list
    """
    file = open("words.txt", 'r')
    words = file.read()
    word_list = words.split("\n")
    file.close()
    choose_word = random.choice(word_list)
    return choose_word

def get_user_input():
    """
    take and return the input from the user as lower
    case
    """
    user_input = input("Enter choice: \n").lower()
    return user_input

def input_validation(user_input):
    """
    validate the input so it can only recieve one
    letter.
    """
    if len(user_input) == 0:
        print("You didn't input anything.")
        return False

    elif not user_input.isalpha():
        print("Invalid: Enter a letter between a to z.")
        return False
    return True


def play_hangman():
    """
    Try the user input against the selected word which
    has been masked. If the user input matches a letter
    in the selected word, the letter will be displayed.
    If not, an attempt is used up.

    Cycle will run till either the word is found or attempts
    are used up.
    """

    selected_word = choose_random_word()
    duplicate_values = []   
    word_mask = []
    attempts_left = 10
    display_instructions()
    print(selected_word)

    for letter in selected_word:
        word_mask.append(letter.replace(letter,'_')) 
    
    while attempts_left > 0:
        print(f"Letters: {len(selected_word)}")
        print(" ".join(word_mask)) 
        user_input  = get_user_input()
       
        if input_validation(user_input):
            if user_input in duplicate_values:
                print(f"'{user_input}' has already been tried.")
                continue
            elif user_input in selected_word: 
                print(f"Good Guess. You found {user_input} in the word")               
                for i in range(len(selected_word)):
                    if selected_word[i] == user_input:
                        word_mask[i] = user_input                     
                if word_mask.count('_') == 0 :
                    print("Well Done, you found it!")
                    print(f"Attempts left: {attempts_left}")                     
                    break            
            else:
                print(f"Incorrect. '{user_input}' is not in the word. Try again!")
                attempts_left -=1
                print(f"Attempts left: {attempts_left}\n")
        duplicate_values.append(user_input) 
    
    if attempts_left == 0:
        print("Game over!")
        print(f"the word was: {selected_word}")
        
       
#display_instructions()
play_hangman()