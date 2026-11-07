print("**========= WELCOME TO THE 95 STARS QUIZ ============** ")
playig = input("Do you want play this game")
if playig !=  "yes":
   quit()
print("okay! let's play this  game")
score = 0
print("*Question 1")
answer = input(" what is capital of india? ")
if True:
 if answer == "newdelhi":
      print("correct")
      score +=1
else :
    print("Incorrect!")
    score -= 1
print("*Question 2")
answer = input(" what is your name?")
if answer =="andrew":
    print("correct!")
    score += 2
else:
    print("Incorrect!")
    score -=1
print("*Question 3") 
answer = input(" what is full form of DSA?")
if answer ==" Data Structre Algorithim":
    print("correct!")
    score += 3
else:
    print("Incorrect!")
    score -=1
print("*Question 4")
answer = input(" what is full sorm of CPU? ")
if answer =="central processing unit":
    print("correct!")
    score += 4
else:
    print("Incorrect!")
    score -=1
print(" your score " + str(score) + "Question correct!=")




 

 



     