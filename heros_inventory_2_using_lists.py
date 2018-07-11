# Heros inventory 2.0
# demos lists

# create a list with some items and display with a for loop
inventory = ["sword", "armor", "shield", "potion"]
print("Your Items: ")

for item in inventory:
    print(item)


# get length of the list
print("You have", len(inventory), "items in your possession.")

# test for membership with in
if "potion" in inventory:
    print("You may heal.")

# display one item through an index
index = int(input("\nEnter the slot number for an item in inventory: "))
print("At slot", index, "is the", inventory[index])

# display slice
start = int(input("\nEnter the slot number to begin a slice: "))
finish = int(input("Enter the slot number to end the slice: "))
print("inventory[", start, ":", finish, "] is the", end="")
print(inventory[start:finish])

#concatenate two lists
chest = ["gold", "gems"]
print("You find a chest which contains:")
print(chest)
print("You add", chest, "to your inventory.")
inventory += chest
print("Your inventory is now: ")
print(inventory)

#assign by index
print("You trade your sword for a longbow.")
inventory[0] = "longbow"
print("Your inventory is now: ")
print(inventory)

#assign via slice
print("You use your gold and gems to buy Yhorms Greatsword.")
inventory[4:6] = "Yhorms Greatsword"
print("Your inventory is now: ")
print(inventory)

#delete an element in a list
print("Yhorms Greatsword broke!  Visit Andre to get it fixed!")
del inventory [4]
print("Your inventory is now: ")
print(inventory)

#delete a slice
print("Your longbow and armor were stolen by thieves!")
del inventory [:2]
print("Your inventory is now: ")
print(inventory)

input("\n\nPress enter to exit")
