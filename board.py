#!/usr/bin/python3
import sys 

#num = input("Enter the size number of the board: ")
def board():
    for x in range(int(3)):
        print("+-----+" * int(3))
        print("|  -  |" * int(3))
        print("+-----+" * int(3))

game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]
y = 0
if y > 100:
    cross = input("Cross Turn: X Type Your Next Move!:  ")      
    circle = input("Circle Turn: O Type Your Next Move!: ")
 

def check():
    global game
    winner_is_1 = True
    winner_is_2 = False
    for i in range(3):
        if  ((game[0][0]) == 1 and (game[0][1]) == 1  and (game[0][2])) == 1 or \
            ((game[1][0]) == 1 and (game[1][1]) == 1  and (game[1][2])) == 1 or \
            ((game[2][0]) == 1 and (game[2][1]) == 1  and (game[2][2])) == 1 or \
            ((game[0][0]) == 1 and (game[1][1]) == 1  and (game[2][2])) == 1 or \
            ((game[0][2]) == 1 and (game[1][1]) == 1  and (game[2][0])) == 1: 
            if winner_is_1:
                print("The Winner is Cross XXX!!")

        if  ((game[0][0]) == 2 and (game[0][1]) == 2  and (game[0][2])) == 2 or \
            ((game[1][0]) == 2 and (game[1][1]) == 2  and (game[1][2])) == 2 or \
            ((game[2][0]) == 2 and (game[2][1]) == 2  and (game[2][2])) == 2 or \
            ((game[0][0]) == 2 and (game[1][1]) == 2  and (game[2][2])) == 2 or \
            ((game[0][2]) == 2 and (game[1][1]) == 2  and (game[2][0])) == 2:
            if winner_is_2: 
                print("The Winner is Circle OOO!!")
        else:
            print("Tie !!")

def crosscheck():
    global cross
    while int(cross) not in [1,2,3,4,5,6,7,8,9]:
        print ("Choose Number Between 1-9 To Be Placed In The Board" )
        cross = input("Cross Turn: X Type Your Next Move!:  ")

def circlecheck():
    global circle
    while int(circle) not in [1,2,3,4,5,6,7,8,9]:
        print ("Choose Number Between 1-9 To Be Placed In The Board" )
        circle = input("Circle Turn: O Type Your Next Move!: ")

def moves():
    global game
    global cross
    global circle
     
    for z in [1,2,3,4,5,6,7,8,9]:
        if int(cross) == z:
            row = (z-1) // 3
            column = (z-1) %3
            game[row][column] = "X"
        if int(circle) == z:
            row = (z-1) // 3
            column = (z-1) %3
            game[row][column] = "O"
    


#Starting
print("You Are Playing Cross Circle Good Luck & Have Fun!! XO")
print(game)
print("Congrats You Are Cross!! X")
cross = input("Cross Turn: X Type Your Next Move!:  ")
crosscheck()
moves()

print(game)

print("Congrats You Are Circle! O")
circle = input("Circle Turn: O Type Your Next Move!: ")
circlecheck()
moves()   
print(game)










 