from random import randint

computer=randint(1,100)

Players_Guess=int(input("Guess the number between 1 to 100 : "))
Guesscount=1
while (computer!=Players_Guess) :


 if(computer > Players_Guess ): 
   print("Guess the number higher than this. ")
 elif(computer < Players_Guess):
   print("Guess the number lower than this. ")

 user_Guess=int(input("Again guess the number as been directed  : "))
 Players_Guess=user_Guess
 
 Guesscount=Guesscount + 1
  
print( f" Congratulations you guess the number {user_Guess} correctly  In { Guesscount} number of tries."  )
