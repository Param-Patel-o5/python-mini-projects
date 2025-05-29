''' Project 0 Rock Paper Scissors'''

import random

computer = random.choice([0, -1, 1])


youstr=input("Enter your gesture:")
youdict={"rock":1,"paper":0,"scissors":-1}
you= youdict[youstr]

# Reverse dictionary to get name from value
reversed_dict = {v: k for k, v in youdict.items()}

if(computer == -1 and you ==1):
 print("you win")

 
elif(computer == -1 and you ==0):
 print("you loose")


if(computer == 0 and you ==1):
 print("you loose")

 
elif(computer == 0 and you ==-1):
 print("you win")


if(computer == 1 and you ==-1):
 print("you loose")

 
elif(computer == 1 and you ==0):
 print("you win")

if(computer == you):
 print("It's a draw.")

print(f"Computer gesture was: {reversed_dict[computer]}")
