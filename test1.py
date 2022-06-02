# Functions go here
class color:
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'
# The Greeting welcomes the user to there quiz. 
def greeting():
    print(color.BOLD +  'Kia ora! Welcome to the Te Reo quiz! \n' + color.END)
    print(color.BOLD + 'Would you like to begin the quiz? \n' + color.END)
    yes1 = input()
    yes1 = yes1.lower()
    if yes1 == "yes": 
        print("\n")
        question1()
    elif "no":
        print("Type yes/no")
    else:
        print("You need to leave")


def question1():
    print(color.UNDERLINE + '1. How do you spell monday in Te Reo? \n' + color.END)
    global score
    ans1 = input()
    ans1 = ans1.lower()
    if ans1 == "mane":
        print(color.BOLD + 'Correct!' + color.END)
        question2()
    else:
        print("Incorrect")

 
def question2():
    print("\n")
    print("How do you spell tuesday in Te Reo?")
    global score
    ans2 = input()
    ans2 = ans2.lower()
    if ans2 == "rarua":
        score += 1
        print("Correct!")
        question3()
    else:
        print("Incorrect")


def question3():
    print(color.BOLD + 'How do you spell wednesday in Te Reo? \n' + color.END)
    global score
    ans3 = input()
    ans3 = ans3.lower()
    if ans3 == "raapa":
        print("Correct!")
        question4()
    else:
        print("Incorrect")


def question4():
    print("\n")
    print("How do you spell thursday in Te Reo?")
    print("HINT: starts with R and ends with E and is a 6 letter word.")
    global score
    ans4 = input()
    ans4 = ans4.lower()
    if ans4 == "rapare":
        print("Correct!")
        question5()
    else:
        print("Incorrect")


def question5():
    print("\n")
    print("How do you spell thursday in Te Reo?")
    print("HINT: starts with R and ends with E and is a 6 letter word.")
    global score
    ans5 = input()
    ans5 = ans5.lower()
    if ans5 == "rapare":
        print("Correct!")
        
    else:
        print("Incorrect")


def end1():
    print("Congratulations! you have passed the quiz with a score of", score, "Great work!")

greeting()
score = 0
question1()

question2()

question3()

question4()

question5()


