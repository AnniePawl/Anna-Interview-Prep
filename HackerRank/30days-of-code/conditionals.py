import math
import os
import random
import re
import sys

""" Given an integer n, perform the following conditional actions:
    - If n is odd, print Weird
    - If n is even and in the inclusive range of 2 to 5 print Not Weird
    - If n is even and in the inclusive range of 6 to 20 , print Weird
    - If n is even and greater than 20, print Not Weird """

def conditionals(N):
    if N % 2 != 0:
        print("Weird")
    elif N % 2 == 0 and N in range(2, 6):
        print("Not Weird")
    elif N % 2 == 0 and N in range(6, 21):
        print("Weird")
    elif N % 2 == 0 and N > 20:
        print("Not Weird")


print(conditionals(5)) # Weird 
print(conditionals(2)) # Not Weird 
print(conditionals(16)) # Weird 
print(conditionals(22)) # Not Weird 