# Counter using tuples and loops
# user enters starting number, ending number, and number by which to count

#define variables asking for necessary user inputs
#check to see if those inputs are integers
#if inputs are integers, continue
#for loop counting starting with the first int, up to second int, counting by the third int


print("\nHello, do you require assistance with counting?")
print("\nPlease tell me what number to start with, the number to count to, and by how much I should count.")

start = int(input("Starting number: "))
end = int(input("Ending number: "))
count_by = int(input("How much to count by: "))

for i in range(start, end, count_by):
    if count_by > start:
        print('Invalide, please try again.')
    elif count_by > end:
        print('Invalid, please try again.')
    print(i)
