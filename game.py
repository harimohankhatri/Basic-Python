# generata the number and let the user guess the number
# if guess is matechd, game win
# if guess is not matched, game lose
# if guess is not in the range, game lose

import random 
def guess_number():
    for i in range(5):
        number = random.randint(1, 10)
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number:
            print("You win!")
        elif guess < 1 or guess > 10:
            print("You lose! The number was", number)
        else:
            print("You lose! The number was", number)
    print("Game over!")
guess_number()