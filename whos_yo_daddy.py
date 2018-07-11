#Who's yo daddy?
#Self-coded

#create dictionary of sons and fathers
#key = son, value = father
#make options to exit, enter name of son to get father, add, replace, and delete son-father pairs

daddy = {"Bill": "Tedd", "Jack": "Jill?", "Rory": "Kyle", "Kevin": "Adam", "Dylan": "Jeremy"}

choice = None
print()


while choice != "0":
    print("""
    
    Who's yo daddy?
    
    0 - Quit Program
    1 - Get daddy for Bill, Tedd, Jack, Rory, Kevin, or Dylan
    2 - add son/father pairing
    3 - replace son/father pairing
    4 - delete son/father pairing
    
    """)
    choice = input("Choice: ")
    print()

    # exit program
    if choice == "0":
        print("Good-bye.")

    # get son/father pairing
    elif choice == "1":
        son = input("Please one of the aforementioned sons: ")
        if son in daddy:
            print (daddy[son])

    # add son/father pairing
    elif choice == "2":
        son = input("What son would you like to add?: ")
        if son not in daddy:
            dad = input("What father would you like me to add?: ")
            daddy[son] = dad
            print("\n", son, "and", dad, "have been added.")
        else:
            print("Son/father pairing already exists.")

    # replace existing son/father pairing with new father
    elif choice == "3":
        son = input("Which son's father would you like to replace?: ")
        if son in daddy:
            dad = input("Who's his new daddy?")
            daddy[son] = dad
            print("\n", son,"'s father has been replaced by", dad)
        else:
            print("Son/father does not exist.")

    # delete father/son pairing
    elif choice == "4":
        son = input("Which son/father pairing would you like to delete?: ")
        if son in daddy:
            del daddy[son]
            print("\n", son, "and his father have been deleted.")

input("\n\nPress enter to exit.")