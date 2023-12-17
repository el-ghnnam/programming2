# GUESS NUMBER (COMPUTER).

from random import randint


# TODO: make project that make a computer guess a number and user should guess what the that computer guessed!.
def user_guess_number(number):
    random_number = randint(1, number)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {number}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Congrats. You have guess the number {random_number} ')


# user_guess_number(10)

# TODO: make project that make a user guess a number and computer should guess what the that user guessed!.

def computer_guess_number(number):
    low = 1
    high = number
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C) ?? ').lower()
        if feedback == 'h':
            high = high - 1
        elif feedback == 'l':
            low = low + 1
    print(f'Congrats, The computer guessed your number, {guess}, correctly!')


computer_guess_number(50)
