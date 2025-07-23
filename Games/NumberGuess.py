import random
def difficulty_selection():
    print("Please choose a difficulty:")
    print("1 - Easy (Guess a number between 1 and 25)")
    print("2 - Medium (Guess a number between 1 and 50)")
    print("3 - Hard (Guess a number between 1 and 75)")
    print("4 - Extreme (Guess a number between 1 and 100)")

    while True:
        option = int(input("Enter 1, 2, 3, 4:"))
        if option == 1:
            return 1, 25, 7
        elif option == 2:
            return 1, 50, 8 
        elif option == 3:
            return 1, 75, 9
        elif option == 4:
            return 1, 100, 10
        else:
            print("Invalid choice, please select 1, 2, 3, 4.")

def game():
    min_num, max_num, max_attempts = difficulty_selection()
    secret_number = random.randint(min_num, max_num)
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"\n🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} tries.\n")
                break
        except ValueError:
            print("Please enter a valid number.")
    
    else:
        print(f"\n💥 Game over! You’ve used all {max_attempts} attempts.")
        print(f"The correct number was {secret_number}.")

def main():
    while True:
        game()
        again = input("Would you like to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing! 👋")
            break
main()
