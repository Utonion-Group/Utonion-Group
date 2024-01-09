#=======================================
#Cup Game by Utonion Group
#=======================================

import random
import time

ran = random.randint(1, 3)
attempts = 1

while True:
    time.sleep(1)
    print("""
    Cup 1            Cup 2            Cup 3            Cup 4            Cup 5
     ___              ___              ___              ___              ___
    /   \            /   \            /   \            /   \            /   \ 
   |     |          |     |          |     |          |     |          |     |
    \___/            \___/            \___/            \___/            \___/

                          In which cup is the ball in?
    """)
    choice = int(input("Cup: "))
    if choice == ran:
        print(f"You're correct! The ball is in cup number {ran}")
        quit()
    elif choice != ran:
        print(f"You're wrong! Try again! ({attempts}/3)")
        attempts += 1
        if attempts == 4:
            print(f"You lose! The cup is in cup number {ran}")
            quit()
