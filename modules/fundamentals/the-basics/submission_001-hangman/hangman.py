#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    # Read the file and display all the words within
    open_file = open(file_name,'r')
    # .readlines() returns a list and list has not attribute .close()
    read_file = open_file.readlines()    
    # Store the list.
    words = read_file
    # Close the file. (Is this a memory leak without closing?)
    open_file.close()

    return words


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    # Random word index
    rand_word_i = random.randint(0,len(words)-1)
    # Correct word
    word = words[rand_word_i]
    # Random character index; -2 to skip /n
    rand_c_i = random.randint(0,len(word)-2)
    # Correct character
    c_char = word[rand_c_i]
    # Slice the indexes
    print('Guess the word: ' + word[:rand_c_i] + "_" + word[rand_c_i+1:])
    """Try this."""
    # replaceLetter = word.replace(word[randomNumberLetter], '_')
    
    return word


def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    # Get the user's guess as input
    answer = input("Guess the missing letter: ")

    return answer


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

