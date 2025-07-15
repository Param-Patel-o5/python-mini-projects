

score=0
print("Welcome to the quiz game!")
print("Type the correct option for the given question.")

answer_1 = input('''Question 1 :  Who was the first President of the United States? 
                  A) Thomas Jefferson 
                  B) Abraham Lincoln  
                  C) George Washington 
                  D) John Adams \n''').upper()

if answer_1 == "C":
 print("Correct!")
 score=score+1
else :
    print("Incorrect. The correct answer is George Washington.")
    

answer_2 = input('''Question 2: What is the capital of Australia?
A) Sydney
B) Melbourne
C) Canberra
D) Perth \n''').upper()

if answer_2 == "C":
 print("Correct!")
 score=score+1
else :
    print("Incorrect. The correct answer is Canberra.")

    
answer_3 = input('''Question 3: Which country has won the most FIFA World Cups?
A) Germany
B) Brazil
C) Argentina
D) Italy \n''').upper()
if answer_3 == "B":
 print("Correct!")
 score=score+1
else :
    print("Incorrect. The correct answer is Brazil.")

answer_4 = input('''Question: Who is the founder of Microsoft?
A) Steve Jobs
B) Jeff Bezos
C) Larry Page
D) Bill Gates
\n
''').upper()

if answer_4 == "D":
 print("Correct!")
 score=score+1
else :
    print("Incorrect. The correct answer is Bill Gates")

answer_5 = input('''Question 5: What is the chemical symbol for Gold?
A) Ag
B) Go
C) Gd
D) Au
\n
''').upper()
if answer_5 == "D":
 print("Correct!")
 score=score+1
else :
    print("Incorrect. The correct answer is Au")


print(f"Your score is {score} out of 5.")


