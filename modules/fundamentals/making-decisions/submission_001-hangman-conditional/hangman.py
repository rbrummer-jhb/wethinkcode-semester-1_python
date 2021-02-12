import random


def read_file(file_name):
    """Returns the lines of the file as a list."""
    with open(file_name) as words:
        return words.readlines()
    

def select_random_word(words):
    """Returns a randomly selected word of the list."""
    random_index = random.randint(0, len(words)-1)
    word = words[random_index]
    return word


def select_random_letter_from(word):
    """
    Returns a randomly selected letter and
    its index from the randomly selected word.
    """
    # - 2 to skip the \n character and select the last character.
    random_index = random.randint(0, len(word)-2)
    letter = word[random_index]

    """Do this to have every instance of the letter hidden."""
    guess_the_word = word.replace(letter, '_')

    """Do this to have only one instance of the letter hidden."""
    # print('Guess the word: ' + word[:random_index] + "_" + word[random_index+1:])

    print('Guess the word: ' + guess_the_word)
    
    return letter, random_index


def get_user_input():
    return input('Guess the missing letter: ')


def show_answer(answer, selected_word, missing_letter_index):
    """
    TODO Step 1 - Show better results messages
    """
    while True:
        if answer == selected_word[missing_letter_index]:
            print(f'The word was: {selected_word}')
            print("Well done! You are awesome!")
            break
        else:
            print(f'The word was: {selected_word}')
            print("Wrong! Do better next time.")
            break

    pass


def ask_file_name():
    """
    TODO Step 2 - Update to prompt user for filename to use for words
    """
    user_file_select = input("Words file? [leave empty to use short_words.txt] : ")
    # Conditional
    if user_file_select == '':
        file_name = "short_words.txt"
    else:
        file_name = user_file_select

    return file_name


def run_game(file_name):
    """
    You can leave this code as is, and only implemented above where the code comments prompt you.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    missing_letter, letter_index = select_random_letter_from(word)
    answer = get_user_input()
    show_answer(answer, word, letter_index)


if __name__ == "__main__":
    words_file = ask_file_name()
    run_game(words_file)

