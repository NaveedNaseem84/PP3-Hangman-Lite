
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

    if not user_input.isalpha():
        print("Invalid: Enter a letter between a to z.")
        return False
    return True



def play_hangman():
    selected_word = choose_random_word()
    print(selected_word)
    attempts_left = 2
    attempts = 0
    user_input = get_user_input()
    validation = input_validation(user_input)

    if(input_validation):
        if user_input == selected_word:
            print("Well done")

    else:
        print("Wrong!")
    
       
#display_instructions()
play_hangman()