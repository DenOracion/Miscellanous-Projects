# A short word game that asks the user to fill in blanks with random words and these words will be used to create a story.
# Consists of three different scenarios
def play_game():
    print("🎉 Welcome to Mad Libs!")
    while True: # Asks the user to select a scenario they want to play
        print("Choose a story:")
        print("1. A Trip to the Zoo")
        print("2. Weird Cafeteria Day")
        print("3. Invention Gone Wrong")
        choice = input("Enter 1, 2, or 3: ")

        if choice == '1':
            scenario_one()
        elif choice == '2':
            scenario_two()
        elif choice == '3':
            scenario_three()
        else:
            print("Invalid choice. Try again.")
            continue

        again = input("Would you like to play another story? (yes/no): ").lower() # After a scenario is played, asks the user if they want to try another one
        if again != "yes": # If they answer no, print out a thank you message for playing the game
            print("Thanks for playing Mad Libs! Goodbye!")
            break

def scenario_one(): # First scenario: A Trip to the Zoo
    # Asks the user to input different adjectives, nouns, and verbs to create the sentence
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun (person, place, thing): ")
    noun2 = input("Enter a noun (person, place, thing): ")
    adjective2 = input("Enter an adjective: ")
    verb1 = input("Enter a verb ending with '-ing': ")
    adjective3 = input("Enter an adjective: ")
    # The sentence that will be printed out
    print(f"Today I went to a {adjective1} zoo.")
    print(f"In a exhibit, I saw a {noun1} named {noun2}.")
    print(f"{noun1} was {adjective2} and {verb1}.")
    print(f"I was {adjective3}!")

def scenario_two(): # Second scenario: Weird Cafeteria Day
    # Scenario two and three will follow a similar format to scenario one, asking the user to input nouns, adjectives, and verbs
    name = input("Enter a name: ")
    food = input("Enter a type of food: ")
    silly_word = input("Enter a silly word: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    # Using the answers given by the user, a sentence will be printed out using the words given
    print(f"{name} walked into the cafeteria and saw a huge pile of {food}.")
    print(f"Suddenly someone shouted '{silly_word}!' and everyone {verb}.")
    print(f"It was the most {adjective} lunch I've ever had!")

def scenario_three(): # Scenario three: Invention Gone Wrong
    # Same format as scenarios one and two
    noun = input("Enter a name for a machine: ")
    verb2 = input("Enter a verb ending with '-ed': ")
    body_part = input("Enter a name of a body part: ")
    animal = input("Enter the name of an animal: ")

    print(f"My {noun} {verb2} me and now I have the {body_part} of the {animal}")

# Starts the game
play_game()

