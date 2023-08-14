from random import *

print('Welcome to the guessing a number game')


def is_valid(guess, limit):
    return True if guess.isdigit() and int(guess) in range(1, limit + 1) else False


def the_game():
    limitation = input('Enter a limitation: ')
    limitation = int(limitation) if limitation.isdigit() and int(limitation) > 1\
                 else all([print('Enter a number'), the_game()])

    num = randint(1, limitation)
    counter = 0
    while True:
        num_guess = input(f'Guess the number in a range from 1 to {limitation}: ')

        if is_valid(num_guess, limitation):
            num_guess = int(num_guess)
            if num_guess > num:
                print('Too much, try again')
                counter += 1
                continue
            elif num_guess < num:
                print('Too few, try again')
                counter += 1
                continue
            else:
                print(f'You guessed the number "{num}", congrats! Number of attempts: {counter}',
                      'Thank you for playing!', sep='\n')
                break
        else:
            print(f'Enter a number in a range from 1 to {limitation}')
            continue


while True:
    the_game()
    if input('Play again? (y/n): ') != 'y':
        break
