import time


def guess_my_number(low, high):
    """Simple guessing game with a command line interface."""
    user = ''
    print(f'\nPlease think of a number between {low} and {high}!')
    time.sleep(3)

    while user != 'c':
        guess = (high + low) // 2
        print(f'\nIs your secret number {guess}?')
        user = input(("\nEnter 'h' to indicate the guess is too high. "
                      "Enter 'l' to indicate the guess is too low. "
                      "Enter 'c' to indicate I guessed correctly. "))
        if user not in 'hlc':
            print('\nSorry, I did not understand your input.')
        else:
            high, low = (high, guess) if user == 'l' else (guess, low)

    print(f'\nGame over. Your secret number was: {guess}')


if __name__ == '__main__':
    guess_my_number(0, 100)
