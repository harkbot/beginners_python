#Print a list of words in random order

    #import random
    #create a constant list of words
    #use random function to generate word order
    #print list of words

import random

WORDS = ["sword", "bow", "shield", "axe", "musket", "knife"]

choice = None



print("""

    Random Word lister
    
    1 - Exit program
    2 - Print the words

""")

while choice == None:
    choice = input("What would you like to do?: ")
    if choice == "1":
        print("Good-bye.")
    elif choice == "2":
        print("Okay here is a random list of words: ")
        random.shuffle(WORDS)
        print(WORDS)
    else:
        print("Invalid user command.")
input("\n\nPress enter to exit.")