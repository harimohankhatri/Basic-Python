#rock paper scissors game
import random
def rock_paper_scissors():
    for i in range (5):
        user_input = input("Enter rock, paper, or scissors: ")
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        if user_input == computer_choice:
            print("It's a tie!")
        elif user_input == "rock" and computer_choice == "scissors":
            print("You win!")
        elif user_input == "paper" and computer_choice == "rock":
            print("You win!")
        elif user_input == "scissors" and computer_choice == "paper":
            print("You win!")
        else:
            print("You lose! The computer chose", computer_choice)
    print("Game over!")
rock_paper_scissors()