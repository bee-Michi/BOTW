import time, sys, random, math
from datetime import datetime
print("Loadng recorces...")
time.sleep(1)
print("Conneccting to servers...")
time.sleep(1)
print("Retrivng memory info...")
time.sleep(2.3)
__copyrigth__ = "©bee_Michi 2021-2022"
__author__ = "bee_Michi"
__version__ = "You are currently in version 1.0! Check if a new update has been relesd!"
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
liscenceCompiler = False
converterPro = False
available = ["Countdown", "Quiz", "Calculator", "Converter", "Guess the number", "Clock", "Password generator", "Liscence compiler!"]
commands = ["Help: This command! Displays all commands", "Copyrigth: Get information about copyrigth", "Liscece: Gives info about the liscence", "Author: Tells you authors and cotntributors of the project!", "Version: Reports on the current version of the program!"]
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
    elif BOTW_SELECT == "liscence compiler":
        liscenceCompiler = True
        break
    elif BOTW_SELECT == "author":
        print(__author__)
        break
    elif BOTW_SELECT == "converter pro":
        converterPro = True
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
    points = 0
    print("Herse the first question")
    print(question1)
    quest1Resp = input()
    if quest1Resp == "central proceccing unit":
        points += 1
    print("Herse the second question")
    print(question2)
    quest2Resp = input()
    if quest2Resp == "random acces memory":
        points += 1
    print("Herse the third question")
    print(question3)
    quest3Resp = int(input())
    if quest3Resp == 2009:
        points += 1
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
elif converterPro == True:
    print("Welcome to converter pro!")
    one_digit_words = {
            '0': ["zero"],
            '1': ["one"],
            '2': ["two", "twen"],
            '3': ["three", "thir"],
            '4': ["four", "for"],
            '5': ["five", "fif"],
            '6': ["six"],
            '7': ["seven"],
            '8': ["eight"],
            '9': ["nine"],
        }

    two_digit_words = ["ten", "eleven", "twelve"]
    hundred = "hundred"
    large_sum_words = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion"]

    def converter(n):
        word = []

        if n.startswith('-'):
            word.append("(negative)")
            n = n[1:]
        
        if len(n) % 3 != 0 and len(n) > 3:
            n = n.zfill(3 * (((len(n)-1) // 3) + 1))

        sum_list = [n[i:i + 3] for i in range(0, len(n), 3)]
        skip = False

        for i, num in enumerate(sum_list):
            if num != '000': skip = False
            
            for _ in range(len(num)):
                num = num.lstrip('0')
                if len(num) == 1:
                    if (len(sum_list) > 1 or (len(sum_list) == 1 and len(sum_list[0]) == 3)) and i == len(sum_list) - 1 and (word[-1] in large_sum_words or hundred in word[-1]):
                        word.append("and")
                    word.append(one_digit_words[num][0])
                    num = num[1:]
                    break

                if len(num) == 2:
                    if num[0] != '0':
                        if (len(sum_list) > 1 or (len(sum_list) == 1 and len(sum_list[0]) == 3)) and i == len(sum_list) - 1:
                            word.append("and")
                        if num.startswith('1'):
                            if int(num[1]) in range(3):
                                word.append(two_digit_words[int(num[1])])
                            else:
                                number = one_digit_words[num[1]][1 if int(num[1]) in range(3, 6, 2) else 0] 
                                word.append(number + ("teen" if not number[-1] == 't' else "een"))
                        else:
                            word.append(one_digit_words[num[0]][1 if int(num[0]) in range(2, 6) else 0] + ("ty " if num[0] != '8' else 'y ') + (one_digit_words[num[1]][0] if num[1] != '0' else ""))
                        break
                    else:
                        num = num[1:]
                        continue
                    
                if len(num) == 3:
                    if num[0] != '0':
                        word.append(one_digit_words[num[0]][0] + " " + hundred)
                        if num[1:] == '00': break
                    num = num[1:]
    
            if len(sum_list[i:]) > 1 and not skip:
                word.append(large_sum_words[len(sum_list[i:]) - 2])
                skip = True
        
        word = " ".join(map(str.strip, word))
        return word[0].lstrip().upper() + word[1:].rstrip().lower() if "negative" not in word else word[:11].lstrip() + word[11].upper() + word[12:].rstrip().lower()

    if __name__ == "__main__":
        while True:
            try:
                n = input("Enter any number to convert it into words or 'exit' to stop: ")
                if n == "exit":
                    break
                int(n)
                print(n, "-->", converter(n))
            except ValueError:
                print("Error: Invalid Number!")