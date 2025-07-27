import random 
emojis = {'r': '🪨', 'p': '📃', 's': '✂️' }
choices = ['r', 'p', 's']

# Tallies how many games the player has won, the computer has won and how many draws occurred
user_score = 0
computer_score = 0
draws = 0
while True: 
    # Presents the scores of the player, computer and how many draws
    print(f"SCORE: You {user_score} - {computer_score} Computer | Draws: {draws}")
    # Asks the player to input rock (r), paper (p), or (s)
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid Choice") # If r, p, or s is not selected, print out invalid choice
        continue
 
    computer_choice = random.choice(choices) # Computer will select one of three choices randomly
    # Prints out what the player chose and what the computer chose
    print(f"You chose{emojis[user_choice]}") 
    print(f"Computer chose{emojis[computer_choice]}")

    #If it is a draw, prints out that the game was a draw and adds a tally to draws
    if user_choice == computer_choice:
        print("It's a draw!")
        draws += 1
    # Game logic: if one of these three occur, then the player gets one point tallied to the user_score
    elif ( 
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print("You win! 🎉")
        user_score += 1
    # If the result is none of the three above, the player loses and the computer_score gets one point tallied
    else:
        print("You lose!")
        computer_score += 1
    
    # Asks the player if they want to play again if y is selected then the entire code is repeated, if n is selected, code moves to the final scores section
    continue_playing = input("Continue? (y/n) ").lower()
    if continue_playing == 'n':
        break

# Prints out the final scores, showing how many times the player won, the computer won and how many draws occurred, plus adding all three together to tally how many games were played in total
print("🏆 FINAL SCORES 🏆")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")
print(f"Draws: {draws}")
print(f"Total games: {user_score + computer_score + draws}")

