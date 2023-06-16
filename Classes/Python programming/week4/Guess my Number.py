# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 00:19:14 2020

@author: Peter
"""

import random

def easy_number(number_guessed):
    easy_rint = random.randint(1, 10)
    if(number_guessed == easy_rint):
        print("Yaay, Correct")
    else:
        print("Nope, my choice was ",easy_rint)
def medium_number(number_guessed):
    medium_rint = random.randint(1, 30)
    if(number_guessed == medium_rint):
        print("Yaay, Correct")
    else:
        print("Nope, my choice was ",medium_rint)

def hard_number(number_guessed):
    hard_rint = random.randint(1, 100)
    if(number_guessed == hard_rint):
        print("Yaay, Correct")
    else:
        print("Nope, my choice was ",hard_rint)


print("Welcome to my number Guessing game!")
print("\n\nPlease select the game level below\n")



game_level = input("1 - Easy\n2 - Medium\n3 - Hard\n")
game_level = int(game_level)


while(True):
    if(game_level == 1):
        number_guessed = input("Guess your number : ")
        easy_number(int(number_guessed))
    elif(game_level == 2):
        number_guessed = input("Guess your number : ")
        medium_number(int(number_guessed))
    elif(game_level == 3):
        number_guessed = input("Guess your number : ")
        hard_number(int(number_guessed))
    else:
        print("You must choose numbers from 1 to 3")
        game_level = input("1 - Easy\n2 - Medium\n3 - Hard\n")
        game_level = int(game_level)
        quit_game = input("Do you want to quit?")
        if(quit_game == "yes" or quit_game == "Yes"):
            break
        