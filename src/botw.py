#This softwere is FOSS or free and open source, so you can look at the source code and make modifications how you please!
#We import the standard modules! Currently the program needs time, sys, random, math and datetime all standar modules that come prepackaged with python!
import time, sys, random, math
from threading import Thread
#Doing some loading to make the softwere look cool!
print("Loadng recorces...")
time.sleep(1)
print("Conneccting to servers...")
time.sleep(1)
print("Retrivng memory info...")
time.sleep(2.3)

#We declere copyrigth, wich includes liscece, ahthor
__copyrigth__ = "©bee_Michi 2021-2022. This softwere is liscenced under the MIT liscence, more information in the liscenece file."
__author__ = "The author of this project is: bee_Michi"
__contributors__ = ""
__version__= "2.0"
versionp = "You are currently in version 2.0! Check if a new update has been relesd on the github page!"

#First messeage
print("------------BOTW------------")

#Help function, to print the avialable utilities
def help():
    #For loops to print the list
    for i in available:
        print(i)
#Commands function, to print the available commands
def commandss():
    #For loops to print the list
    for i in commands:
        print(i)

#Countdown function. We will need it later to intialaize the functions!
def countdownI():
    #Central countdown function.
    def countdown(t):
        #We calculate minutes and seconds
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins,secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        #Print this when the timer ends
        print("Timer completed!")
    #Input for time (in seconds!)
    t = input("Welcome to countdown! Enter the time in seconds: ")
    #And we call the function
    countdown(int(t))
#Clock
def clock():
    #Get now using datetime
    currT = time.localtime()
    #Set the current time
    curr_clock = time.strftime("%H:%M:%S", currT)
    #Final print!
    print("The current time is:", curr_clock)
def liscenceCompiler():
    #Get some info like year and copyrigth owner
    year = input("Welcome to mit liscence compiler! Please input the year: ")
    copy_owner = input("Input the copyrigth owner: ")
    #We print the liscence
    print(
        f"""        Copyright (c) {year} {copy_owner}
        Permission is hereby granted, free of charge, to any person
        obtaining a copy of this software and associated documentation
        files (The softere), to deal in the Software without
        restriction, including without limitation the rights to use,
        copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the
        Software is furnished to do so, subject to the following conditions:
        
        The above copyright notice and this permission notice shall be
        included in all copies or substantial portions of the Software.
        
        THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND,
        EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
        OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
        HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
        WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
        FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
        OTHER DEALINGS IN THE SOFTWARE.
    """)
def calculator():
    first_number = int(input("Welcome to converter! Plese insert the first number: "))
    print("insert the second number")
    second_number = int(input("Please insert the second number: "))
    operation =  input("Insert the operation. (the supported operation are addition, subtraction, multiplications, division): ")
    if operation == "addition":
        final = first_number + second_number
    elif operation == "subtratcion":
        final = first_number - second_number
    elif operation == "multiplication":
        final = first_number * second_number
    elif operation == "division":
        final = first_number / second_number
    else:
        print("Not a supperted operation!")
        sys.exit()
    print("The result is " + str(final))
def quiz():
    print("loading questions and selecting questions")
    time.sleep(2)
    question1 = "What does cpu stand for"
    question2 = "What does ram stand for"
    question3 = "In what year did micheal jackson die?"
    points = 0
    print("Hello and welcome to quiz!")
    print("We are about to lanch you in!")
    time.sleep(0.7)
    print(f"First question {question1}")
    quest1Resp = input("Respond here: ")
    if quest1Resp == "central processing unit":
        points += 1
    print(f"Second question: {question2}")
    quest2Resp = input("Respond here: ")
    if quest2Resp == "random access memory":
        points += 1
    print(f"Third question {question3}")
    quest3Resp = input("Respond here: ")
    if quest3Resp == "2009":
        points += 1
    print("Your points are...")
    print(str(points))
    if points == 3:
        print("You got maximun points")
    elif points == 2:
        print("You got medimu points")
    elif points == 1:
        print("You got ok points")
def converter():
    select_conversion = input("Welcome to converter! Plese insert your conversion (The supported conversions are: int to string, float to string, string to int, string to float): ")
    if select_conversion == "int to string":
        insert = int(input("Plese insert the int: "))
        print(f"Conversion = {str(insert)} ")
    elif select_conversion == "float to string":
        insert = float(input("Plese insert the float: "))
        print(f"Conversion = {str(insert)} ")
    elif select_conversion == "string to int":
        insert = input("Plese insert the str: ")
        print(f"Conversion = {int(insert)} ")
    elif select_conversion == "string to float":
        insert = input("Plese insert the str: ")
        print(f"Conversion = {float(insert)} ")
def gtn():
    print("Welcome to guess the number!")
    number = random.randint(1, 10)
    attempts = 3
    responese = ["You got it first try", "Pretty good", "Saved on corner!"]
    while attempts != 0:
        numResp = int(input("Please input a number between 1, 10: "))
        if numResp == number:
            if attempts == 3:
                top = responese[0]
            elif attempts == 2:
                top = responese[1]
            elif attempts == 1:
                top = responese[2]    
            print(f"You won! {top}")
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
    if attempts == 0:
        print("You lost! It will be for next time!")
def passwordgen():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    special = "@#$%&*¡¿±£/!¶§{}[]Ç"
    
    pass_len = int(input("Welcome to password generator! Enter the password length: "))
    pass_amount = int(input("Input the number of passwords you want: "))
    print("Generating...")
    time.sleep(1)
    for pas in range(pass_amount):
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
        print(f"Herse your password: {gen_password}")
def fullCPU():
    class MyThread(Thread):
        def __init__(self, name,):
            Thread.__init__(self)
            self.name = name
    def run(self):
        for i in range(1000000):
            msg = "%s is running" % \
                self.name
            print(msg)
    def create_threds():
        for i in range(10000):
            name = "Thread #%s" % (i + 1)
            my_thread = MyThread(name)
            my_thread.start()
    if __name__ == "__main__":
        create_threds()
def rng():
    digit_choice = int(input("Welcome to random number generator! Please insert the lenght of the number (acceepted up to 7): "))
    print("Generating")
    time.sleep(1.2)
    while True:
        if digit_choice > 7:
            print("Not accepted digit!")
            break
        elif digit_choice < 0:
            print("Not accepted digit!")
            break
            
        if digit_choice == 1:
            rng_1 = random.randint(0 , 9)
            print(rng_1)
            break
        elif digit_choice == 2:
            rng_2 = random.randint(10 , 99)
            print(rng_2)
            break
        elif digit_choice == 3:
            rng_3 = random.randint(100 , 999)
            print(rng_3)
            break
        elif digit_choice == 4:
            rng_4 = random.randint(1000 , 9999)
            print(rng_4)
            break
        elif digit_choice == 5:
            rng_5 = random.randint(10000 , 99999)
            print(rng_5)
            break
        elif digit_choice == 6:
            rng_6 = random.randint(100000 , 999999)
            print(rng_6)
            break
        elif digit_choice == 7:
            rng_7 = random.randint(1000000 , 9999999)
            print(rng_7)
            break
def rpc():
    while True: 
        player_choice = input("Welcome to rock paper sciccors! Choose your wepon (r for rock, p for paper, s for sciccors): ")
        if player_choice!="r" and player_choice!="p" and player_choice!="s":
                print("error, letter not corresponding!")
                break
        print("Ok, the algorithim is choosing his wepon")
        time.sleep(1.5)
        #computer algorithim
        computer = random.randint(0,2)
        if computer==0:
            computer = "rock"
        elif computer== 1:
            computer = "paper"
        elif computer == 2:
            computer = "siscors"
        thanks = "Thanks for playing!"
        if player_choice == computer:
            print(f"The computer chose {computer}. The final result is a draw. {thanks}")        
            break
        elif player_choice =="r" and computer=="siscors" or player_choice=="s" and computer=="paper" or player_choice=="p" and computer=="rock":
            print(f"The computer chose {computer}. So you won! GG! {thanks}")   
            break
        else:
            print(f"The computer chose {computer} so he won, it will be for next time! {thanks}")
            break
#List of all utilities available!
available = {
            "Countdown: A simple countdown ⏲", 
            "Quiz: How much do you know, test your skills in quiz ❓", 
            "Calculator: Need a calculator, we gotha fam 🧮", 
            "Converter: convert an int/float to string and viceversa 💯->100", 
            "Guess the number: Try to guess the super ai tottaly not randomly generated number 🤖", 
            "Clock: Gets the current time 🕰", 
            "Password generator: Generate secure passwords 🔑", 
            "Liscence compiler:  Easaly compile liscences 📖",
            "Rock paper sciccors: A decades old game, now in a computer cli! 🖥",
            "Random number generator: Generate number up to 7 digits long 🤯",
            "Pranker: Prank your firends, make it seem like there CPU is at 100% 💾"
            }

commands = {"Help: Displays all utilities ❓", "Commands: This command! Displays all commands 🤖", "Copyrigth: Get information about copyrigth and the liscence 📖", "Author: Tells you authors and cotntributors of the project! 🖥", "Contributors: The peapole hwo helped with this project 👬"}
#The central input
while True:
    BOTW_SELECT = input("Welcome! Input help to learn about the available utilites or command for useful commands, or exit to exit: ")
    if BOTW_SELECT == "countdown":
        countdownI()
    elif BOTW_SELECT == "clock":
        clock()
    elif BOTW_SELECT == "liscence compiler":
        liscenceCompiler()
    elif BOTW_SELECT == "version":
        print(versionp)
    elif BOTW_SELECT == "calculator":
        calculator()
    elif BOTW_SELECT == "quiz":
        quiz()
    elif BOTW_SELECT == "guess the number":
        gtn()
    elif BOTW_SELECT == "password generator":
        passwordgen()
    elif BOTW_SELECT == "help":
        help()
    elif BOTW_SELECT == "commands":
        commandss()
    elif BOTW_SELECT == "exit":
        sys.exit("Exiting...")
    elif BOTW_SELECT == "quit":
        sys.exit("Exiting...")
    elif BOTW_SELECT == "converter":
        converter()
    elif BOTW_SELECT == "random number generator":
        rng()
    elif BOTW_SELECT == "rock paper sciccors":
        rpc()
    elif BOTW_SELECT == "pranker":
        fullCPU()
    elif BOTW_SELECT == "random number generator":
        rng()
    elif BOTW_SELECT == "rock paper sciccors":
        rpc()
