#Word Jumble

#the computer picks a random word and then "jumbles" it
#player has to guess the original word

import random

#create a sequence of words to choose from
WORDS = ("python", "jumble", "coding", "diarrhea", "answer", "macaroni")

#pick one word randomly from the sequence
word = random.choice(WORDS)

#creat a var to use later to see if guess is correct
correct = word

#pseudocode for word jumble algorithm
    #create an empty jumble word
    #while the chosen word has letters in it
        #extract a random letter from the chosen word
        #add the random letter to the jumble word

#create a jumbled version of the word
jumble =  ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word =word[:position] + word[(position + 1):]

#welcome player to the game
print("""
    
        Welcome to Word Jumble!
        Unscramble the letters and make a word.
        (Press Enter key at prompt to quit.
""")

print("The jumble is:", jumble)

#get the player to guess the word
guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")

#congratulate the player
if guess == correct:
    print("You've got it, you're a winner!")

print("Thanks for playing!")

input("\n\nPress enter to exit.")