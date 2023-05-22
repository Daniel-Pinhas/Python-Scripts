#!/usr/bin/python3

import sys

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
is_draw = 0

def board():
    for x in range(3):
        print("+-----+" * 3)
        print(("|  {}  |" * 3).format(*[game[x][y] if game[x][y] != 0 else "-" for y in range(3)]))
        print("+-----+" * 3)

def check():
    global game
    global is_draw
    # Check rows
    if (game[0][0] == game[0][1] == game[0][2] == "X") or \
       (game[1][0] == game[1][1] == game[1][2] == "X") or \
       (game[2][0] == game[2][1] == game[2][2] == "X"):
        print("The Winner is Cross XXX!!")
        sys.exit(1)
    elif (game[0][0] == game[0][1] == game[0][2] == "O") or \
         (game[1][0] == game[1][1] == game[1][2] == "O") or \
         (game[2][0] == game[2][1] == game[2][2] == "O"):
        print("The Winner is Circle OOO!!")
        sys.exit(1)

    # Check columns
    if (game[0][0] == game[1][0] == game[2][0] == "X") or \
       (game[0][1] == game[1][1] == game[2][1] == "X") or \
       (game[0][2] == game[1][2] == game[2][2] == "X"):
        print("The Winner is Cross XXX!!")
        sys.exit(1)
    elif (game[0][0] == game[1][0] == game[2][0] == "O") or \
         (game[0][1] == game[1][1] == game[2][1] == "O") or \
         (game[0][2] == game[1][2] == game[2][2] == "O"):
        print("The Winner is Circle OOO!!")
        sys.exit(1)

    # Check diagonals
    if (game[0][0] == game[1][1] == game[2][2] == "X") or \
       (game[0][2] == game[1][1] == game[2][0] == "X"):
        print("The Winner is Cross XXX!!")
        sys.exit(1)
    elif (game[0][0] == game[1][1] == game[2][2] == "O") or \
         (game[0][2] == game[1][1] == game[2][0] == "O"):
        print("The Winner is Circle OOO!!")
        sys.exit(1)
    is_draw += 1    
    if is_draw == 9:
        print("It's a draw!")
        sys.exit(1)
      
dumps = set()

def crosscheck():
    global cross
    global dumps
    while int(cross) not in range(1, 10) or int(cross) in dumps:
        if int(cross) in dumps:
            print("Already Played..")
        else:
            print("Choose a number between 1-9 to be placed on the board.")
        cross = input("X: Cross Turn Type Your Next Move!: ")

def circlecheck():
    global circle
    global dumps
    while int(circle) not in range(1, 10) or int(circle) in dumps:
        if int(circle) in dumps:
            print("Already Played..")
        else:
            print("Choose a number between 1-9 to be placed on the board.")
        circle = input("O: Circle Turn Type Your Next Move!: ")
  
def movescross():
    global game
    global cross
    global dumps
    for z in range(1, 10):
        if int(cross) == z:
            row = (z - 1) // 3
            column = (z - 1) % 3
            game[row][column] = "X"
            dumps.add(int(cross))

def movescircle():
    global game
    global circle
    global dumps
    for z in range(1, 10):
        if int(circle) == z:
            row = (z - 1) // 3
            column = (z - 1) % 3
            game[row][column] = "O"
            dumps.add(int(circle))

# Starting
print("You Are Playing Cross Circle! Good Luck & Have Fun!! XO")
board()
# Cross Introduction
print("Congrats You Are Cross!! X")
cross = input("X Cross Turn Type Your Next Move! From 1-9: ")
crosscheck()
movescross()
board()
check()
# Circle Introduction
print("Congrats You Are Circle! O")
circle = input("O Circle Turn Type Your Next Move! From 1-9: ")
circlecheck()
movescircle()
board()
check()
while True:
    cross = input("X: Cross Turn Type Your Next Move!: ")
    crosscheck()
    movescross()
    board()
    check()
    circle = input("O: Circle Turn Type Your Next Move!: ")
    circlecheck()
    movescircle()
    board()
    check()
