# Things needed for the file to work
import pickle
import itertools
import threading
import time
import operator 
import sys
import random
from time import sleep
import os
os.system("cls")

# Idk what this is but it looks cool
print ("╱╱┏╮")
print("╱╱┃┃")
print("▉━╯┗━╮")
print("▉┈┈┈┈┃")
print("▉╮┈┈┈┃")
print("╱╰━━━╯")

# Asks what you want to do.
answer = input ("Do you want to play or calculate? p / c ")

        #Calculator
if answer == "c":
    
    print('Calculator v1.0 (Python 3.6.2)')
    ans = input('Hello! Are you here for calculating?(y/n) ')
    if ans == 'y':
     print('OK! LOADING...')
     sleep(0.8)
    elif ans == 'n':
     print("Oh, you're not going ahead... OK.")
     sleep(4.2)
     quit()
    op = {'+':operator.add,
      '-':operator.sub,
      '*':operator.mul,
      '/':operator.truediv}


    num1 = int(input('Input 1st number: '))
    method = op[input('Input symbol(+,-,*,/):')]
    num2 = int(input('Input 2nd number: '))

    ans = method(num1,num2)

    print('Answer is ', ans)
# The Game Thing
if answer == "p":

    ans = input("Hello! Let's play rock paper scissors! Yes or No? ")

    if ans == "No": #If you quit :/
        print("Oh, ok. Goodbye!")
        sleep(4.2)
        quit()

    if ans == "Yes" or "y" or "yes" "Y":


        done = False
    #This is the "animation"
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rLoading ' + c)
                sys.stdout.flush()
                time.sleep(0.05)


    t = threading.Thread(target=animate)
    t.start()


    time.sleep(3)
    done = True
    # The Game Code of Rock Paper Scissors 
    possible_actions = [" rock", " paper", " scissors"]
    computer_action = random.choice(possible_actions)
    ans = input("Rock, Paper or Scissors? ")  
    print(f"\nYou chose {ans}, computer chose{computer_action}.\n")
    if ans == computer_action:
        print(f"Both players selected{ans}. It's a tie!")
        sleep(4.2)
    elif ans == " rock" or " Rock":
        if computer_action == " scissors":
            print("Rock smashes scissors! You win!")
            sleep(4.2)

        else:
            print("Paper covers rock! You lose.")
            sleep(4.2)
    elif ans == " paper" or " Paper":
        if computer_action == " rock":
            print("Paper covers rock! You win!")
            sleep(4.2)
        else:
            print("Scissors cuts paper! You lose.")
            sleep(4.2)
    elif ans == " scissors":
        if computer_action == " paper":
            print("Scissors cuts paper! You win!")
            sleep(4.2)
            
        else:
            print("Rock smashes scissors! You lose.")
            sleep(4.2)
# And thats the end I suppose.
# I'll update this code every 1 or 2 weeks depending on some factors lol
#Thanks a lot if you made it this far!! :P 