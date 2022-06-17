

# Te Reo Quiz - Hunter Murray - Simon / 13/05/2022
# Sequence 1 / Greeting / V1 / Hunter

score = 0

print("Enter Your Name Below.")
name = input("")
print("Kia Ora!", name, "Welcome to the Te Reo quiz.")
print("\n")
question1 = input("Would you like to begin the quiz? ").lower()
print("\n")

# Sequence 2 / Question 1 / V2 / Hunter / 15/05/2022
if question1 == "yes":
  print("1. How do you spell - Monday - in Te Reo \n",
       "A. Mane \n",
       "B. Matanga \n",
       "C. Teranga")

else:
    print("You have missed out on the rambunctious quiz.")

answer1 = input("").lower()

if answer1 == "a":
    score += 1
    print("Correct")
    print("You have earnt", score, "score!")

else:
    print("Incorrect! the answer was A")
print("\n")

# Sequence 3 / Question 2 / V3 / Hunter / 17/05/2022
print("2. What is - Tuesday - in Te Reo \n",
     "A. Raapa \n",
     "B. Rarua \n",
     "C. Takimichi \n")

answer2 = input("").lower()

if answer2 == "b":
    score += 1
    print("Correct")
    print("You have earnt", score, "score!")

else:
    print("Incorrect! the answer was B")
print("\n")

# Sequence 4 / Question 3 / V4 / Hunter
print("What is - Wednesday - in Te Reo? \n",
     "A. Ataarangi \n",
     "B. Matanga \n",
     "C. Raapa \n")

answer3 = input("").lower()

if answer3 == "c":
    score += 1
    print("Correct")
    print("You have earnt", score, "score!")

else:
    print("Incorrect! the answer was C")
print("\n")

# Sequence 5 / Question 4 / V5 / Hunter
print("What is - Wednesday - in Te Reo? \n",
     "A. Mataarnga \n",
     "B. Raapa \n", 
     "C. Taarnga")

answer4 = input("").lower()

if answer4 == "b":
    score += 1
    print("Correct")
    print("You have earnt", score, "score!")

else:
    print("Incorrect! the answer was B")
print("\n")

#Sequence 6 / Question 5 / V6 / Hunter

print("What is - Thursday - in Te Reo? \n",
     "A. Tangi \n",
     "B. Ruapetua \n", 
     "C. Rapare ")

answer5 = input("").lower()

if answer5 == "c":
    score += 1
    print("Correct")
    print("You have earnt", score, "score!")

else:
    print("Incorrect! the answer was C")

# Sequence 7 / Writtin Question 1 / V7 / Hunter
# In this question the user has to input a written out answer for a right answer.
print("\n")
print("Can you write - Friday - in Te Reo?")

answer6 = input("").lower()

if answer6 == "paraire":
    score += 1
    print("Correct")
    print("You have earnt", score, "score!")

else:
    print("Incorrect! It is spelt as - Paraire -")

#Conclusion / V8 / Hunter / 17/05/2022 
print("\n")
print("Congratulations you have passes the quiz! Your score was:", score, "out of 6, Great Work!")