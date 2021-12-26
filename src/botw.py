import time, sys, random, math
from datetime import datetime
print("Loadng recorces...")
time.sleep(1)
print("Conneccting to servers...")
time.sleep(1)
print("Retrivng memory info...")
time.sleep(2.3)
__copyrigth__ = "©bee_Michi 2021-2022. This softwere is liscenced under the MIT liscence, more information in the liscenece file."
__author__ = "bee_Michi"
__version__= "1.1"
version = "You are currently in version 1.1! Check if a new update has been relesd on the github page!"
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
paswwordG = False
liscenceCompiler = True
available = {"Countdown: A simple countdown", 
            "Quiz: How much do you know, test your skills in quiz", 
            "Calculator: Need a calculator, we gotha fam", 
            "Converter: convert an int/float to string", 
            "Guess the number: Try to guess the super ai tottaly not randomly generated number", 
            "Clock: Gets the current time", 
            "Password generator: Generate secure passwords", 
            "Liscence compiler:  Easaly compile liscences"
            }
commands = ["Help: This command! Displays all commands", "Copyrigth: Get information about copyrigth", "Liscece: Gives info about the liscence", "Author: Tells you authors and cotntributors of the project!", "Version: Reports on the current version of the program!"]
while True:
    if BOTW_SELECT == "copyrigth":
        print(__copyrigth__)
        break
    elif BOTW_SELECT == "version":
        print(version)
        break
    elif BOTW_SELECT == "exit":
        sys.exit()
    elif BOTW_SELECT == "countdown":
        countdownS = True
        break
    #!Quiz is broken, therphore no acces unless modifictation!
    elif BOTW_SELECT == "calculator":
        calculator = True
        break
    elif BOTW_SELECT == "converter":
        converter = True
        break
    elif BOTW_SELECT == "help":
        for i in commands:
            print(i)
        print("Are you looking for the available utilities?")
        break
    elif BOTW_SELECT == "guess the number":
        gtn = True
        break
    elif BOTW_SELECT == "clock":
        clock = True
        break
    elif BOTW_SELECT == "password generator":
        paswwordG = True
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
    question1 = "What does cpu stand for"
    question2 = "What does ram stand for"
    question3 = "In what year did micheal jackson died?"
    question4 = "How many years did the second world war last?"
    question5 = "What's the name of the cracker of the enigma code?"
    question6 = "Who is the cofounder of microsoft?"
    time.sleep(1.2)
    print("questions loaded")
    time.sleep(0.5)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Herse the first question")
    print(question1)
    quest1Resp = input()
    print("Herse the second question")
    print(question2)
    quest2Resp = input()
    print("Herse the third question")
    print(question3)
    quest3Resp = input()
    points = 0
    if quest1Resp == "central proccecing unit" and quest2Resp == "random acces memory" and quest3Resp == "2009":
        points += 3
    elif quest1Resp == "central proceccing unit" and quest2Resp == "random acces memory" and quest3Resp != "2009":
        points += 2
    elif quest1Resp == "central proceccing unit" and quest2Resp != "random acces memory" and quest3Resp != "2009":
        points += 1
    elif quest1Resp != "central proceccing unit" and quest2Resp == "random acces memory" and quest3Resp != "2009":
        points += 1
    elif quest1Resp != "central proceccing unit" and quest2Resp != "random acces memory" and quest3Resp == "2009":
        points += 1
    elif quest1Resp != "central proceccing unit" and quest2Resp == "random acces memory" and quest3Resp == "2009":
        points += 2
    elif quest1Resp == "central proceccing unit" and quest2Resp != "random acces memory" and quest3Resp == "2009":
        points += 2
    print("Your points are...")
    print(str(points))
    if points == 3:
        print("You got maximun points")
    elif points == 2:
        print("You got medimu points")
    elif points == 1:
        print("You got ok points")    
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
    print("Plese insert the int/float")
    if select_conversion == "int":
        insert = int(input())
    elif select_conversion == "float":
        insert = float(input())
    print("Converting")
    time.sleep(0.5)
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
elif paswwordG == True:
    print("Welcome to password generator!")
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    special = "@#$%&*"
    pass_len = int(input("Enter Password Length"))
    print("Generating...")
    time.sleep(2)
    alpha_len = pass_len//2
    num_len = math.ceil(pass_len*30/100)
    special_len = pass_len-(alpha_len+num_len)
    password = []
    def generate_pass(length, array, is_alpha=False):
        for i in range(length):
            index = random.randint(0, len(array) - 1)
            character = array[index]
            if is_alpha:
                case = random.randint(0, 1)
                if case == 1:
                    character = character.upper()
            password.append(character)



    generate_pass(alpha_len, alpha, True)
    generate_pass(num_len, num)
    generate_pass(special_len, special)
    random.shuffle(password)
    gen_password = ""
    for i in password:
        gen_password = gen_password + str(i)
    print("Herse your password:")
    print(gen_password)
elif liscenceCompiler == True:
    print("Welcome to mit liscence compiler!")
    print("Input the year")
    year = int(input())
    print("Input the copyrigth owner!")
    copy_owner = input()
    print("Input the name of the softwere!")
    softwere_name = input()
    year_str = str(year)
    print(f"Copyright (c) {year_str} {copy_owner}")
    print("Permission is hereby granted, free of charge, to any person")
    print("obtaining a copy of this software and associated documentation")
    print(f"files for {softwere_name}, to deal in the Software without")
    print("restriction, including without limitation the rights to use,")
    print("copy, modify, merge, publish, distribute, sublicense, and/or sell")
    print("copies of the Software, and to permit persons to whom the")
    print("Software is furnished to do so, subject to the following conditions:")
    print("")
    print("The above copyright notice and this permission notice shall be")
    print("included in all copies or substantial portions of the Software.")
    print("")
    print("THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND,")
    print("EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES")
    print("OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND")
    print("NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT")
    print("HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,")
    print("WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING")
    print("FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR")
    print("OTHER DEALINGS IN THE SOFTWARE.")
