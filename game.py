import random
print("----- WELCOME TO THE 'ROCK, PAPER, SCISSOR' GAME -----" )

# Creating List
choices = ["rock", "paper", "scissor"]
# Taking user Input
player = input("Choose rock, paper, scissor :-").lower()
#Computer choosing random from the list
computer = random.choice(choices)
#creating condition for different.....
if player == computer:
    print(f"It's a Tie both chosses {player}")

elif player == "rock" and computer == "scissor":
    print(f"You Win! {player} beats {computer}")

elif player == "scissor" and computer == "paper":
    print(f"You Win! {player} beats {computer}")

elif player == "paper" and computer == "rock":
    print(f"You Win! {player} beats {computer}")

else:
    print(f"Computer Win! {computer} beats {player}")