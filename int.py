import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)  # Use random.choice to get a single element
player = None

# Mapping shorthand to actual choices
input_mapping = {"r": "rock", "p": "paper", "s": "scissors"}

while player not in input_mapping.values():  # Check against the actual choices
    player_input = input("r, p, or s?: ").lower()
    if player_input in input_mapping:
        player = input_mapping[player_input]

print("computer:", computer)
print("player:", player)

# Determine the winner
if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "scissors" and computer == "paper") or \
     (player == "paper" and computer == "rock"):
    print("Player wins!")
else:
    print("Computer wins!")
