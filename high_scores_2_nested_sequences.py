# Hugh scores 2.0
# demos nested sequences

scores = []

choice = None
while choice != "0":
    print("""
    
    High Scores 2.0 
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    
    """)
    choice = input("Choice: ")
    print()

    if choice == "0":
        print("Bye.")

    # display high-score table:
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # add a score
    elif choice == "2":
        name = input("What is the players' name?: ")
        score = int(input("What score did they get?: "))
        entry = (name, score)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # keeps only the top 5 scores

    # unknown user input
    else:
        print("Invalid choice.")

input("\n\nPress enter to exit.")