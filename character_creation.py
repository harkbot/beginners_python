# Character creator

# Welcome player to game
# get name of character from user
# define how many points user starts with
# define what attributes points can be added to
# give player option to check, add, remove points from given attribute

points = 30

attributes = {"health": 0, "strength": 0, "dexterity": 0, "intelligence": 0}

while False:
    print("You have", points, "left!")

choice = None
while choice != "0":
    print("""
    
    Greetings traveller.  We are going to need to update your records as you are new to Vinheim.
    Please choose from the following options.
    Note you have 30 attribute points.
    
    0 - Exit Character Creator
    1 - Check attributes (Health, Strength, Dexterity, Intelligence)
    2 - Add points to attribute
    3 - Remove points from attribute
    
    """)

    choice = input("Choice: ")
    print()


    # exit game
    if choice == "0":
        print("Good-bye.")

    # check attributes
    if choice == "1":
        print(attributes)

    # add to attributes
    elif choice == "2":
        attribute = input("Add points to: health, strength, dexterity, or intelligence ?")
        if attribute in attributes:
           add = int(input("How many points?: "))
           attributes[attribute] += add
           print(attribute, "now has", add, "points.")
           points -= add
           print
           print("You have", points, "remaining.")
           print
        else:
            print("You do not possess this trait!")

    # remove attribute points
    elif choice == "3":
        attribute = input("Remove points from: health, strength, dexterity, or intelligence?")
        if attribute in attributes:
            subtract = int(input("Remove how many points?: "))
            if attributes[attribute] > subtract:
                attributes[attribute] -= subtract
                print(attribute, "now has", subtract, "points.")
                points += subtract
                print()
                print("You have", points, "remaining.")
                print()
            elif attributes[attribute] < subtract:
                print("You don't have enough points in given attribute!")
                print()
                print("You have", points, "remaining.")
                print()



input("\n\nPress Enter to Exit.")

