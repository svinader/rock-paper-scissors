#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#

import random

ROCK = "1"
SCISSOR = "2"
PAPER = "3"

print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Enter 1 for Rock, 2 for Scissor, or 3 for Paper: ")
computer_choice = str(random.randint(1, 3))
print("Computer chose:", computer_choice)
if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == ROCK and computer_choice == SCISSOR)
    or (user_choice == SCISSOR and computer_choice == PAPER)
    or (user_choice == PAPER and computer_choice == ROCK)
):
    print("You win!")
else:
    print("You lose!")