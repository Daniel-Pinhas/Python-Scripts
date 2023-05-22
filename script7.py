#!/usr/bin/python3


factors = []
M = int(input("Enter a number "))  # number whose factors we need to find
for N in range(1, M + 1):
    if M % N == 0:  # remainder is zero
        factors.append(N)
print("Factors of {} are {}".format(M, factors))
