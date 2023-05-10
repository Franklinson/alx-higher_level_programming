#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastNumber = 0

if number >= 0:
    LastNumber = number % 10

else:
    LastNumber = (-number % 10) * -1

if LastNumber > 5:
    print(f"Last digit of {number} is {LastNumber} and is greater than 5")

if LastNumber == 0:
    print(f"Last digit of {number} is {LastNumber} and is 0")

if (LastNumber < 6) and (LastNumber != 0):
    print(f"Last digit of {number} is {LastNumber} and is less than 6 and not 0")
