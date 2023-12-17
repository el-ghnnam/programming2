from random import choice

from words import words
import string

# TODO: make Game called hangman you lost if the guy are complete constructed by the mistakes you had make.

def get_valic_word(words):
    word = choice(words)    # randomly chooses something from the words list
    while '_' in word or ' ' in word:
        word = choice(words)

    return word.upper()

def hangman():
    word = get_valic_word(words)
    word_letters = set(word)    # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you  have used these letters: ', ' '.join(used_letters))
        # tell user what current is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1       # takes away a life if wrong.
                print('Letters is not in the word.')


        elif user_letter in used_letters:
            print('You have already use that character. Please try again.')
        else:
            print('Invalid character. Please try again. ')
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died., sorry. the word was ', word)
    else:
        print('You guessed the word', word, '!!')



# user_input = input('Type something: ')
# print(user_input)

hangman()