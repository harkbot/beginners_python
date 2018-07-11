#Geek translator
#demos dictionaries

geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
        "Googling": "searching the internet for knowledge that you do not currently possess.",
        "Keyboard plaque": "collection of debris found in and around your keyboard",
        "Link rot": "the process by which web page links become obsolete.",
        "Percussive maintenance": "the act of striking an electronic device to make it work.",
        "Uninstalled": "Being fired because you suck ass."}

choice = None
while choice != "0":
    print("""
    
        Geek Dictionary
        
        0 - Quit
        1 - Look up a Geek term
        2 - Add a Geek term
        3 - Redefine a Geek term
        4 - Delete a Geek term
    
    """)

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # get a term
    elif choice == "1":
        term = input("What term do you want returned?: ")
        if term in geek:
            definition = geek[term]
            print("/n", term, "means", definition)
        else:
            print("Sorry, that term does not exist.")

    # add a term to geek dictionary
    elif choice == "2":
        term = input("What term would you like me to add?: ")
        if term not in geek:
            definition = input("\nWhat is the definition?: ")
            geek[term] = definition
            print("\n", term, "has been added")
        else:
            print("That term already exists, try again.")

    # redefine a term in geek
    elif choice == "3":
        term = input("What term should be redefined?: " )
        if term in geek:
            definition = input("What is the new definition?: ")
            geek[term] = definition
            print("The term has been redefined.")
        else:
            print("This term is not in Geek dictionary.")

    # deleting a term in geek
    elif choice == "4":
        term = input("What term should be deleted?: ")
        if term in geek:
            del geek [term]
            print("\n", term, "has been deleted.")
        else:
            print("That term is not in Geek dictionary.")

    # unknown user input
    else:
        print("Invalid choice, please try again.")

input("\n\nPress enter key to exit.")