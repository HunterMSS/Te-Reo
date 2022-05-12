# Te Reo Quiz - Hunter Murray - Simon
#Sequence 1 / Greeting / V1 / Hunter

score = 0

print("Kia Ora! Welcome to the Te Reo quiz.")

print("\n")

question1 = input("Would you like to begin the quiz? ").lower()

print("\n")

if question1 == "yes":
  print("1. How do you spell - Monday - in Te Reo? ")


answer1 = input("").lower()

if answer1 == "mane":
    score += 1
    print("Correct")
    print("score", score)

else:
    print("Incorrect")

print("\n")
    
question2 = input("What is - Tuesday - in Te Reo? ")

answer2 = input("").lower()

if answer2 == "rarua":
    score += 1
    print("Correct")
    print("score", score)

    







