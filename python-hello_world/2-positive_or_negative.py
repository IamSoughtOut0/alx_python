#!/usr/bin/python3
import random
number = random.randint(-10, 10)
import random

def generate_random_signed_number():
    return random.randint(-10, 10)

def check_number_sign(number):
    if number > 0:
        return "is positive"
    elif number == 0:
        return "is zero"
    else:
        return "is negative"

if __name__ == "__main__":
    number = generate_random_signed_number()
    print("The number:", number, "-", check_number_sign(number))



