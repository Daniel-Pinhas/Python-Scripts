#!/usr/bin/python3
import string
import random
import sys



l = input("Enter a letter to find out what is the word!: ")
def letcheck():
    global l
    while l not in string.ascii_letters or l == " ":
        print("Please Enter One letter..")
        l = input("Enter a letter to find out what is the word!: ")
        dumps.append(l)
letcheck()


def get_list_of_words(path):
    with open('hangman.txt', 'r', encoding='utf-8') as f:
        return f.read().splitlines()

words = get_list_of_words('hangman.txt')
random_word = random.choice(words)
#print(random_word)
lst = [*random_word]
lst2 = [*'*'*len(lst)]

mistake = 0
dumps = []

def hangman():
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    global mistake 
    print(HANGMANPICS[mistake])
              
while True:
    if l not in lst:
        print("Wrong! The Letter isnt in the Random Word")
        hangman()
        mistake += 1
        if mistake == 7:
            print('''
                    █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█
                    █▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄
                                                        ''')
            sys.exit(1)
        l = input("Enter a letter to find out what is the word!: ")
        dumps.append(l)
        letcheck()
        while l in dumps:
            print("You Already Guessed This Letter")
            l = input("Enter a letter to find out what is the word!: ")
            letcheck()
    else:
        print("Correct! The letter is in the Random Word")
        for i in range(len(lst)):
            if l == lst[i]:
                lst2[i] = l
        print ("".join(lst2))
        if "*" not in lst2:
            print('''
                   █▀▀ ▀▄▀ █▀▀ █▀▀ █░░ █░░ █▀▀ █▄░█ ▀█▀  
                   ██▄ █░█ █▄▄ ██▄ █▄▄ █▄▄ ██▄ █░▀█ ░█░  
            
                     █▄█ █▀█ █░█    █░█░█ █▀█ █▄░█ █ █
                     ░█░ █▄█ █▄█    ▀▄▀▄▀ █▄█ █░▀█ ▄ ▄
                                                        ''')
            sys.exit(1)  
        l = input("Enter a letter to find out what is the word!: ")
        letcheck()

        while l in lst2 or l in dumps:
            print("You Already Guessed This Letter")
            l = input("Enter a letter to find out what is the word!: ")
            letcheck()

