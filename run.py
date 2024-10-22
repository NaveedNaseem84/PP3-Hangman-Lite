
import random

# code to import from file adapted from CI love sandwiches module.and
# Will be referenced accordingly in Readme.md
# Used in display_instructions and choose_random_word def's below

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
    words = file.read().lower()
    word_list = words.split("\n")
    file.close()
    choose_word = random.choice(word_list)
    return choose_word

def mask_selected_word(selected_word):
    """
    mask the letters in the randomly selected 
    word with _
    """
    word_mask = []
    for letter in selected_word:
        word_mask.append(letter.replace(letter,'_'))
    return word_mask

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
     valid letter.
    """
    if len(user_input) == 0:
        print("You didn't input anything.")
        return False

    elif len(user_input) > 1:
        print("Only one letter allowed!")
        return False 

    elif not user_input.isalpha():
        print("Invalid: Enter a letter between a to z.")
        return False
    return True  

def letter_found(user_input, selected_word, word_mask):
    """
    update the masked letter with the correct found one
    """
    print(f"Good Guess. You found '{user_input}' in the word")             
    for i in range(len(selected_word)):
        if selected_word[i] == user_input:
            word_mask[i] = user_input   

def letter_not_found(user_input, attempts_left):
    """
    If the input letter is wrong, deduct 1 from the attempts
    """
    print(f"Incorrect. '{user_input}' is not in the word. Try again!")
    attempts_left-=1
    print(f"Attempts left: {attempts_left}") 
    return attempts_left


def game_over(selected_word, attempts_left):
    """
    Summary of game when lost.
    """
    print("==============================================")
    print("               G A M E  O V E R ")
    print("                Attempts left: 0")
    print(f"              The word was: {selected_word}")    
    print("==============================================")

def game_won(selected_word, attempts_left):
    """
    Summary of the game when won.
    """
    print("===============================================")
    print("             W E L L  D O N E !")
    print(f"             Attempts left: {attempts_left}")
    print(f"            The word was: {selected_word}")    
    print("===============================================")

def set_difficulty():
    """
    Take valid input for the difficulty level and return it as a value
    ready for the play hangman function to use.

    For the purpose of this game the following attempt values are used:
    easy = 12, medium = 8, hard = 4
    """
    print("Choose your difficulty:")
    print("1 = easy, 2 = medium, 3 = hard") 
    difficulty_list = [1,2,3]     
    while True:
        try:
            difficulty = (get_user_input())
            if difficulty == "1":
                attempts_left = 12                
            elif difficulty == "2":
                attempts_left = 8                
            elif difficulty == "3":
                attempts_left = 4
            elif not difficulty in difficulty_list:
                print("Invalid. 1 = easy, 2 = medium, 3 = hard")
                continue                  
        except:
            print("Invalid. 1 = easy, 2 = medium, 3 = hard")
            continue
        else:
            return attempts_left      

def play_hangman():
    """
    Try the user input against the selected word which
    has been masked. If the user input matches a letter
    in the selected word, the letter will be displayed.
    If not, an attempt is used up.

    Cycle will run till either the word is found or attempts
    are used up.
    """
    display_instructions()
    attempts_left = set_difficulty()    
    selected_word = choose_random_word()
    word_mask = mask_selected_word(selected_word)
    duplicate_values = []          
    print(selected_word) # remove in final version!
    print(f"Total Attempts: {attempts_left}")

    while attempts_left > 0:             
        print(" ".join(word_mask)+"\n")
        print(f"Letters: {len(selected_word)}")
        print("type 'help' for instructions")            
        user_input  = get_user_input()
        if user_input =="help":
            display_instructions()
            continue       
        elif input_validation(user_input):
            if user_input in duplicate_values:
                print(f"'{user_input}' has already been tried.")
                continue
            duplicate_values.append(user_input)
            if user_input in selected_word:                          
                letter_found(user_input, selected_word, word_mask)
                if word_mask.count('_') == 0:
                    won = game_won(selected_word, attempts_left)                                   
                    #play_hangman()
                    break           
            else:
               attempts_left = letter_not_found(user_input, attempts_left)           
    if attempts_left == 0:         
        lost = game_over(selected_word, attempts_left)
        #play_hangman()
        

play_hangman()