import numpy as np
import pandas as pd
from random import randint

b = randint(1,100)
a=-1
guesses = 0
while a != b:
        guesses = guesses + 1
        a = int(input("Please enter a number from 1 t0 100: "))
        if a == b:
            print("Correct!")
        elif a > b :
            print("try a little lower")
        else :
            print("try a little upper")

print("You have got it")
print(f"Guesses =: {guesses}")