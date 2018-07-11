#Hero's Inventory
#Demos tuple creation

#create an empty tuple
inventory = ()

#treat tuple as a condition
if not inventory:
    print("You are empty-handed.")

#create tuple with items
inventory = ("sword", "shield", "armor", "healing potion")

#print the tuple
print("\nThe tuple inventory is:")
print(inventory)

#print each element of the tuple
print("\nYour items:")
for item in inventory:
    print(item)

#get the length of a tuple
print("\nYou have", len(inventory), "items in your possession.")

#test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

#display one item through an index
index = int(input("\nEnter the index number for an item in your inventory: "))
print("At index", index, "is", inventory[index])

#concatenate tuples
chest = ("gold", "gems")
print("You find a chest.  It contains:  ")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now: ")
print(inventory)

input("\n\nPress Enter to exit.")

