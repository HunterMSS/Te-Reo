#Base quiz learning code / Hunter / 9/07/2022 V3
print(" Welcome to the Te Reo Quiz \n",
    "Please input a letter to answer the question. \n")

#importing the random libary
import random

#score
score = 0

#global and quesitons lists
english = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "wednesday",  "tuesday", "saturday"]
right_answer = ["mane", "rarua", "raapa", "rapare", "paraire", "maika", "ratapu", "raapa", "rarua", "maika"]
option_1 = ["raatapu" , "Paaranga" , "rahori", "manurere", "taika", "miraka", "raiona", "matupa", "peru", "taki"]
option_2 = ["ruapatu" , "maki " , "taupau", "ruarua", "rorohika", "pounamu", "tanga", "kiore", "mohiti", "hako"]

#defines a function to generate a question / Hunter / 9/07/2022 V3
def generate_question(english, right_answer, option_1, option_2):

#global score allows me to modify a variable outside of the current scope / Hunter / 9/07/2022 V3
  global score
  print("Type the correct letter for", english , "in maori")
  random_sequence = random.randint(0,2)
    
#seperate print statements for readability / Hunter / 9/07/2022 V3
  if (random_sequence == 0):
    print("A.", option_1)
    print("B.", option_2)
    print("C.", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
      print("Correct! \n")
    else:
      print("incorrect! The Answer Was", right_answer, " \n")

  elif (random_sequence == 1):
    print("A.", option_1)
    print("B.", right_answer)
    print("C.", option_2)
    answer = input().lower()
    if answer == "b":
      score += 1
      print("Correct! \n")
    else:
      print("Incorrect! The Answer Was", right_answer, " \n")
    

  elif (random_sequence == 2):
    print("A.", right_answer)
    print("B.", option_2)
    print("C.", option_1)
    answer = input().lower()
    if answer == "a":
      score += 1
      print("Correct! \n")
    else:
      print("Incorrect! The Answer Was", right_answer, " \n")

  elif (random_sequence == 3):
    print("A.", option_1)
    print("B.", right_answer)
    print("C.", option_2)
    answer = input().lower()
    if answer == "b":
      score += 1
      print("Correct! \n")
    else:
      print("Incorrect! The Answer Was", right_answer, " \n")

  elif (random_sequence == 4):
    print("A.", right_answer)
    print("B.", option_1)
    print("C.", option_2)
    answer = input().lower()
    if answer == "a":
      score += 1
      print("Correct! \n")
    else:
      print("Incorrect! The Answer Was", right_answer, " \n")

  elif (random_sequence == 5):
    print("A.", option_2)
    print("B.", option_1)
    print("C.", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
      print("Correct! \n")
    else:
      print("Incorrect! The Answer Was", right_answer, " \n")

  elif (random_sequence == 6):
    print("A.", right_answer)
    print("B.", option_1)
    print("C.", option_2)
    answer = input().lower()
    if answer == "a":
      score += 1
      print("Correct! \n")
    else:
      print("Incorrect! The Answer Was", right_answer, " \n")

  elif (random_sequence == 7):
    print("A.", option_2)
    print("B.", option_1)
    print("C.", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
      print("Correct! \n")
    else:
      print("Incorrect! The Answer Was", right_answer, " \n")

  elif (random_sequence == 8):
    print("A.", right_answer)
    print("B.", option_1)
    print("C.", option_2)
    answer = input().lower()
    if answer == "a":
      score += 1
      print("Correct! \n")
    else:
      print("Incorrect! The Answer Was", right_answer, " \n")

  elif (random_sequence == 9):
    print("A.", option_2)
    print("B.", option_1)
    print("C.", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
      print("Correct! \n")
    else:
      print("Incorrect! The Answer Was", right_answer, " \n")

  elif (random_sequence == 10):
    print("A.", option_2)
    print("B.", right_answer)
    print("C.", option_1)
    answer = input().lower()
    if answer == "b":
      score += 1
      print("Correct! \n")
    else:
      print("Incorrect! The Answer Was", right_answer, " \n")

#How many times it will generate the lists and show questions. / Hunter / 9/07/2022 V3
for i in range (0, 10):
  generate_question(english[i],right_answer[i],option_1[i],option_2[i])
    
#Shows the user their score / Hunter / 9/07/2022 V3
print("You score", score)

#If the score is above 6 they have passed / Hunter / 9/07/2022 V3
if score >= 6:
    print("Congratulations! You have passed.")
    
#if the users score is below 4 they fail / Hunter / 9/07/2022 V3
if score <= 4:
    print("You scored below 4, You have failed.")
    