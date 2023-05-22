#!/usr/bin/python3
import string
import random
import sys

l = input("Enter a letter to find out what is the word!: ")

while l not in string.ascii_letters :
    print("Please Enter One letter..")
    l = input("Enter a letter to find out what is the word!: ")


def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

words = get_list_of_words('/usr/share/dict/words')
random_word = random.choice(words)
print(random_word)
lst = [*random_word]
lst2 = [*'*'*len(lst)]

mistake = 0
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
    
dumps = []
          
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

        while l in dumps:
            print("You Already Guessed This Letter")
            l = input("Enter a letter to find out what is the word!: ")
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
        while l in lst2:
            print("You Already Guessed This Letter")
            l = input("Enter a letter to find out what is the word!: ")


