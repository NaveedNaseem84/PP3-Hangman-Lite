
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
    list using the new line as split. 
    Randomly select a word from this list
    """
    file = open("words.txt", 'r')
    words = file.read()
    word_list = words.split("\n")
    file.close()

    random_word = random.choice(word_list)
    print(random_word)
    print(len(random_word))

    
#display_instructions()
choose_random_word()