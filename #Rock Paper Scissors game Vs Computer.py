#Rock Paper Scissors game Vs Computer
import random

user_input = input("Pick Rock, Paper, Scissors").lower()
computer_options= ['rock','paper','scissors']
computer_choice= random.choice(computer_options)
print(f"\nYou chose {user_input}, computer chose {computer_choice}.\n")


if user_input==computer_choice:
    print(f"It's a tie! Both players selected {user_input}. ")

elif user_input == 'rock':
    if computer_choice=='scissors':
        print("Rock destroys Scissors; You win!")
    else:
        print("Paper Covers Rock; Computer wins!")

elif user_input == 'scissors':
    if computer_choice=='paper':
        print("Scissor cuts Paper; You win!")
    else:
        print("Rock destroys Scissors; Computer wins!")

elif user_input == 'paper':
    if computer_choice=='rock':
        print("Paper Covers Rock; You win!")
    else:
        print("Scissor Cuts Paper; Computer wins!")



