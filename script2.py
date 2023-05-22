#!/usr/bin/python3

print("abcdefg"[::-1])

x=input("a string:")

def palindrome(string):
    if (string[::-1]) == (string):
        return "palindrome"
    else:
        return "not a palindrome"

print(palindrome(x))


