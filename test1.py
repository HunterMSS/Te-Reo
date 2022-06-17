#Color and fonts used for decorating text for a more better feel of the quiz. 
class color:
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m' 
# Functions go here
# The Greeting welcomes the user to there quiz.
# 10/06/2022
def greeting():
    print(color.UNDERLINE + "Please Enter Your Name Below:" + color.END)
    name = input("")
    print(color.UNDERLINE + "Kia Ora " + name +  "! Welcome To The Te Reo Quiz! Do You Want To Participate In This Quiz? " + color.END)
    yes1 = input()
    yes1 = yes1.lower()
    if yes1 == "yes":
        print("\n")
        question1()
    elif yes1 == "no":
        print("You quit").sys.exit
    else:
         print("No quiz for you.")

#Question 1 / 17 / 06 / 2022 / Hunter / V3
def question1():
    print(color.BOLD + "1. How would spell Monday in Te Reo? \n" + color.END,
         "A. mane \n",
         "B. manaanga \n",
         "C. tangaa")
    ans1 = input()
    ans1 = ans1.lower()
    if ans1 == "mane":
        print('Correct!')
        question2()
    elif ans1 == "manaanga" or ans1 == "tangaa":
        print("Incorrect")
        question2()
    else:
        print("Incorrect, Please choose one of the options. \n")
        question1()

#Question 2 / 17 / 06 / 2022 / Hunter / V2
def question2():
    print("\n")
    print(color.BOLD + "2. How would spell Tuesday in Te Reo? \n" + color.END,
         "A. tangaa \n",
         "B. rarua \n",
         "C. raapa")
    ans2 = input()
    ans2 = ans2.lower()
    if ans2 == "rarua":
        print("Correct!")
        question3()
    elif ans2 == "a" or ans2 == "c":
        print("Incorrect")
        question3()
    else:
        print("Please choose one of the options. \n")
        question2()

#Question 3 / 17/ 06 / 2022 / Hunter / V3
def question3():
    print("\n")
    print(color.BOLD + "3. How would you spell Wednesday in Te Reo? \n" + color.END,
         "A. raapa \n",
         "B. tapanga \n",
         "C. rapare")
    ans3 = input()
    ans3 = ans3.lower()
    if ans3 == "raapa":
        print("Correct!")
        question4()
    elif ans3 == "tangaa" or ans3 == "rapare":
        print("Incorrect")
        question4()
    else:
        print("Please choose one of the options. \n")
        question3()

#Question 4 / 17/ 06 / 2022 / Hunter / V3
def question4():
    print("\n")
    print(color.BOLD + "4. How would you spell Thursday in Te Reo? \n" + color.END,
         "A. rapare \n",
         "B. rarua \n",
         "C. raapa")
    ans4 = input()
    ans4 = ans4.lower()
    if ans4 == "rapare":
        print("Correct!")
        question5()
    elif ans4 == "rarua" or ans4 == "raapa":
        print("Incorrect")
        question4()
    else:
        print("Please choose one of the options. \n")
        question4()

#Question 5 / 17/ 06 / 2022 / Hunter / V3
def question5():
    print("\n")
    print(color.BOLD + "5. How would you spell Friday in Te Reo? \n"+ color.END,
         "A. Paraire \n",
         "B. Faatanga \n",
         "C. Ropuku")
    ans5 = input()
    ans5 = ans5.lower()
    if ans5 == "paraire":
        print("Correct!")
        end1()
    elif ans5 == "" or ans5 == "":
        print("Incorrect")
    else:
        print("Please choose one of the options. \n")
        question5()

#End Function / 17 06 / 2022
def end1():
    print("Congratulations! you have passed the quiz!")

greeting()

question1()

question2()

question3()

question5()

end1()
