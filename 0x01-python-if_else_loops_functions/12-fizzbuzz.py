#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 15 == 0:
            print("FizzBuzz", end="")
        elif n % 5 == 0:
            print("Buzz", end="")
        elif n % 3 == 0:
            print("Fizz", end="")
        else:
            print(n, end="")

        print(" ", end="")
