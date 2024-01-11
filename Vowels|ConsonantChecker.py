#==========================================
#Vowels/Consonant Checker by Utonion Group
#==========================================

text = input("Enter a string: ")
vowels = 0
consonants = 0
for char in text.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1
print(f"Vowels: {vowels}, Consonants: {consonants}")
