#=======================================
#Reverse Sentence/Word by Utonion Group
#=======================================

choice = input("Sentence here: ")
words = choice.split()
e = " ".join(words[::-1])
print(e)

choice2 = input("Word here: ")
e = choice2[::-1]
print(e)
