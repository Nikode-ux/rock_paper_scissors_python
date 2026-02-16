import random

options = ["rock", "paper", "scissors"]


player = input("Choose rock, paper, or scissors.")
computer = random.choice(options)

print("You chose:", player)
print("Computer chose:", computer)

if player not in options:
    print("Invalid choice")
elif player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You win")

elif player == "scissors" and computer == "paper":
    print("You win!")

elif player == "paper" and computer == "rock":
    print("You win!")

else:
    print("Computer wins!")