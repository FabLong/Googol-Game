#Imports
import time
import random

#VERY! Early Access
print("VERY! Early Access\n")
print("Game no longer includes an actual Googol\n")
#Assign List
numbers = []

#Googol Value
googol = 10**10

#Quick Rules:
print("Welcome To: GOOGOL\n")
print("How to play:\n")
print("Random numbers on each card will be displayed.")
print("You will be shown them 1 at a time.")
print("You have to decide if the card you have just been given is the card with the highest value")
print("If you get this correct you win. Goodluck!")

#Number of playing Cards
cards = int(input("How many cards would you like to play with?"))


#Choosing Gamemode (Potential value of numbers)
choice = ("")
while choice not in ("Y", "N", "y", "n"):
    choice = str(input("Easy mode: Y | N "))

if choice == ("Y") or choice == ("y"):
    googol = 100

#Generate random numbers
for i in range(cards):
    numbers.append(random.randint(1, googol))

#Assign Values
my_value = 0
choice = ""
#Display numbers + Choosing
for i in range(len(numbers)):
    #Card number
    print("Card number:" + str(i + 1))
    #Display number
    print (numbers[i])

    #Ask user if they believe this is the largest number
    while choice not in ("Y", "N", "y", "n"):
        choice = str(input("Do you think this is the largest number? Y | N" ))

    #Breaking loop if number is believed to be largest number and storing chosen number
    if choice == ("Y") or choice == ("y"):
        my_value = numbers[i]
        break
    choice = ""

#If did not choose number, last value is assigned to my_value
if my_value == 0:
    my_value = numbers[-1]

#Print Player Number
print("Your number is:" + str(my_value))

#Assign Values
max_number = my_value

#Finding actual largest number
for i in range(len(numbers)):
    if max_number < numbers[i]:
        max_number = numbers[i]

#Print Max Number
print("The Max Number is:" + str(max_number))

#Who Won?
if max_number == my_value:
    print("You win!")
else:
    print("You lose!")







