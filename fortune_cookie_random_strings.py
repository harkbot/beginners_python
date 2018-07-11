#user opens the fortune cookie
#5 different fortunes, one is assigned to the user at random


import random

print("\tHerro!!! Wercome to my Chinese Restaurant!")
print("\tPrease open Fortune Cookie! (type yes to open cookie)")

FORTUNE = ("You will be bedridden", "You will die alone", "Nobody loves you", "You will drown", "You will be happy forever!")

cookie = random.choice(FORTUNE)
open = str(input("Open cookie? "))

if open is "yes":
    print(cookie)


input("\n\nPress Enter to Exit!")