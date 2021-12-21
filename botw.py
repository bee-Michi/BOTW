import time, sys, random
from datetime import datetime
print("Loadng recorces...")
time.sleep(1)
print("Conneccting to servers...")
time.sleep(1)
print("Retrivng memory info...")
time.sleep(2.3)
__copyrigth__ = "©bee_Michi 2021-2022"
__author__ = "bee_Michi"
__version__ = "0.2"
print("Welcome to BOTW or best over time waster")
print("Type help to get a list abot all available utilities")
print("Copyrigth can be acces with the copyrigth command")
print("And the current version can be accesed with the version command")
print("Or input exit to exit")
BOTW_SELECT = input()

countdownS = False
quiz = False
calculator = False
converter = False
gtn = False
clock = False
available = ["countdown", "quiz", "calculator", "converter"]
while True:
    if BOTW_SELECT == "copyrigth":
        print(__copyrigth__)
        break
    elif BOTW_SELECT == "version":
        print(__version__)
        break
    elif BOTW_SELECT == "exit":
        sys.exit()
    elif BOTW_SELECT == "countdown":
        countdownS = True
        break
    elif BOTW_SELECT == "quiz":
        quiz = True
        break
    elif BOTW_SELECT == "calculator":
        calculator = True
        break
    elif BOTW_SELECT == "converter":
        converter = True
        break
    elif BOTW_SELECT == "help":
        for i in available:
            print(i)
        break
    elif BOTW_SELECT == "get the number":
        gtn = True
        break
    elif BOTW_SELECT == "clock":
        clock = True
        break
if countdownS == True:
    print("Welcome to countdown!")
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins,secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print('Timer completed!')
    #We ask the lengh
    t = input('Enter the time in seconds: ')
    #We print the timer
    countdown(int(t))
elif quiz == True:
    print("Hello and welcome to quiz")
    print("Do you need a reminder of the rules?")
    get_rules = input("input y or n: ")
    if get_rules == "y":
        print("The rules are simple")
        print("You are asked 3 questions")
        print("You need to respond to them")
        print("After responding all 3 questions you will get how many points you have!")
        print("3 is best, 2 is better, 1 is ok, 0 is loss")
        print("Try to get 3 points!")
    else:
        print("Ok!")
    print("loading questions")
    time.sleep(1.7)
    print("selecting questions")
    time.sleep(3)
    question = ["What does cpu stand for", "What does ram stand for?", "In what year did micheal jackson died?", "How many years did the secon world war last?"]
    quest_select = 3
    while quest_select != 0:
        random.choice(question)
        quest_select -= 1
    time.sleep(1.2)
    print("questions loaded")
    time.sleep(0.5)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
elif calculator == True:
    print("Welcome to calculator")
    print("Instert the first number")
    first_number = int(input())
    print("insert the second number")
    second_number = int(input())
    print("Insert the operation")
    print("(the supported operation are addition, subtraction, multiplications, division)")
    operation =  input()
    if operation == "addition":
        final = first_number + second_number
    elif operation == "subtratcion":
        final = first_number - second_number
    elif operation == "multiplication":
        final = first_number * second_number
    elif operation == "division":
        final = first_number / second_number
    print("The result is " + str(final))
elif converter == True:
    print("Welcome to converter!")
    print("Selcect the opeartion")
    print("Supported are: int to string, float to str")
    select_conversion = input()
    print("Plese insert")
    insert = int(input())
    print("Conversion = " + str(insert))
elif gtn == True:
    print("Welcome to guess the number!")
    print("Want to have a refresh on the rules?")
    rules_refresh = input()
    if rules_refresh == "y":
        print("You have 3 attempts to get the number!")
        print("The number is randomly genrated!")
        print("Try to get it!")
    elif rules_refresh == "n":
        print("Okey!")
    print("generating")
    time.sleep(2)
    print("Number generated")
    print("Input a number between 1, 10")
    number = random.randint(1, 10)
    attempts = 3
    responese = ["You got it first try", "Pretty good", "Saved on corner!"]
    while attempts != 0:
        numResp = int(input())
        if numResp == number:
            print("You won")
            break
        elif numResp < number:
            print("Try again, and a little higer")
            attempts -= 1
        elif numResp > number:
            print("Try again, and a little lower")
            attempts -= 1
        else:
            print("Not a number between 1 and 10")
            attempts -= 1
    if attempts == 3:
        print(responese[0])
    elif attempts == 2:
        print(responese[1])
    elif attempts == 1:
        print(responese[2])
    else:
        print("You lost")
elif clock == True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)