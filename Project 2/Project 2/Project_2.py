# Project 2: Guessing Game
# Nhan Nguyen
# ITM 313 - Python

#Allow to use random and time function
import random
import time

#Introduce the game rule
print("Welcome to Guessing a Lucky Number Game !!!")
print("You have 5 attempts to guess the lucky Number")
print("The Lucky Number will generate from 0 to 20")
print("")

#Generate a Lucky Number from 0 to 20 
luckynum = random.randint(0,20)
print("You have 30 seconds to guess")

#Countdown clock, user has 30 seconds to guess
now = time.time()
time_limit = 30
end_time = now + time_limit

#Count user attempts
attempts = 10   
while attempts != 0:
    #Ask user to guess a numer
    num = input("Enter Your Lucky Number: ")
    print("")
    if not num.isdigit():
        #for i in range(10):
        print("ERROR: Please Enter a Proper Number")
        print("")
    else:
        value = eval(num)
        #Display a message if user put a number that greater than 20
        if value > 20:
            print("EROOR: Please Enter a Number From 0 to 20")
            print("")
        else:
            attempts -= 1
            #Timer
            if time.time() >= end_time:
                print("Sorry, time is up")
                print("GAME OVER!!")
                break
            #hint
            if value > luckynum:
                print("Your guessing number is high")
            if value < luckynum:
                print("Your guessing number is low")
            #if user guess correct then display message
            if value == luckynum:
                print("Congratulation! Your lucky number is" , luckynum)
                print("")
                break
            #show how many attempts that user has left
            if attempts != 0:
                print("You have", attempts ,"guesses left")
        #Display a messsage if user run out of attempts
        if attempts == 0:
            print("You have tried all your guesses - Good luck next time!!")
            print("GAME OVER!!!")


