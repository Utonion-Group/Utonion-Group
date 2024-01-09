#=======================================
#Factorials by Utonion Group
#=======================================

import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
while True:
    try:
        choice = int(input("Enter a positive number: "))
        time.sleep(1)
        if choice < 0:
            raise ValueError("Please enter a positive number!")
    except ValueError as error:
        print(f"Error: {error}")
    else:
        fac = factorial(choice)
        print(f"Factorial of {choice} is {fac}")
        time.sleep(1)
        choice2 = input("Do you want to repeat the code?(y/n): ").lower()
        if choice2 == "y":
            time.sleep(1)
        else:
            print("Goodbye!")
            quit()
