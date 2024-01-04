import time

alphabet_n = ["N", "n"]
alphabet_y = ["Y", "y"]

while True:
    choice = input("Word: ").lower()
    reverse_word = ""

    for char in choice:
        reverse_word = char + reverse_word

    if reverse_word == choice:
        print(f"{choice}({reverse_word}) is a palindrome")
        time.sleep(1)
        print("Do you want to exit? (y/n)")
        choice2 = input(">>")
        if choice2 in alphabet_y:
            print("Okay, goodbye!")
            quit()
        elif choice2 in alphabet_n:
            time.sleep(1)
    elif reverse_word != choice:
        print(f"{choice}({reverse_word}) isn't a palindrome")
