#!/usr/bin/python3

import sys

player1 = input("Player1 Go Play!: Rock Paper Scissors Shoot: ")

if player1 in ("paper" ,"rock" , "scissors"):
    pass
else:
    print("You must choose rock paper or scissors!")
    sys.exit(1)

player2 = input("Player2 Go Play!: Rock Paper Scissors Shoot: ")

if player2 in ("paper" , "rock" , "scissors"):
    pass
else:
    print("You must choose rock paper or scissors!")
    sys.exit(1)  


if str(player1) == "rock" and str(player2) == "paper":
        print("Player2 You Won!")
elif str(player1) == "paper" and str(player2) == "rock":
        print("Player1 You Won!") 
elif str(player1) == "paper" and str(player2) == "scissors":
        print("Player2 You Won!") 
elif str(player1) == "scissors" and str(player2) == "paper":
        print("Player1 You Won!")     
elif str(player1) == "rock" and str(player2) == "scissors":
        print("Player1 You Won!") 
elif str(player1) == "scissors" and str(player2) == "rock":
        print("Player2 You Won!")
else:
      print("Teko")