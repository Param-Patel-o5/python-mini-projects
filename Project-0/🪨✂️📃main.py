import random

gesture = ["rock", "paper", "scissors"]
youdict = {"rock": 1, "paper": 0, "scissors": -1}
reversed_dict = {v: k for k, v in youdict.items()}

# Get computer's gesture
computer = random.choice(list(youdict.values()))

# Get user's gesture with validation
youstr = None
while youstr not in youdict:
    youstr = input("Enter your gesture (rock, paper, or scissors): ").lower()

you = youdict[youstr]

# Game logic
if computer == you:
    result = "It's a draw."
elif (you - computer == 1) or (you - computer == -2):
    result = "You win!"
else:
    result = "You lose."

print(result)
print(f"Computer gesture was: {reversed_dict[computer]}")
