import random

class DiceGame:
    def __init__(self):
        self.total_rolls = 0
        self.roll_sum = 0
        self.highest_roll = 0
        self.lowest_roll = 12
        self.doubles_count = 0
        self.roll_history = []
        self.max_history = 10
    
    def roll_dice(self):
        """Roll two dice and update statistics"""
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_total = die1 + die2
        
        # Update statistics
        self.total_rolls += 1
        self.roll_sum += roll_total
        self.highest_roll = max(self.highest_roll, roll_total)
        if self.total_rolls == 1:  # First roll
            self.lowest_roll = roll_total
        else:
            self.lowest_roll = min(self.lowest_roll, roll_total)
        
        if die1 == die2:
            self.doubles_count += 1
        
        # Update history (keep only last 10 rolls)
        self.roll_history.append((die1, die2, roll_total))
        if len(self.roll_history) > self.max_history:
            self.roll_history.pop(0)
        
        return die1, die2, roll_total
    
    def show_statistics(self):
        """Display current game statistics"""
        if self.total_rolls == 0:
            print("No rolls yet!")
            return
        
        avg_roll = self.roll_sum / self.total_rolls
        print("\n=== ROLL STATISTICS ===")
        print(f"Total rolls: {self.total_rolls}")
        print(f"Average roll: {avg_roll:.2f}")
        print(f"Highest roll: {self.highest_roll}")
        print(f"Lowest roll: {self.lowest_roll}")
        print(f"Doubles rolled: {self.doubles_count}")
        print(f"Doubles percentage: {(self.doubles_count/self.total_rolls)*100:.1f}%")
    
    def show_history(self):
        """Display recent roll history"""
        if not self.roll_history:
            print("No roll history yet!")
            return
        
        print("\n=== ROLL HISTORY ===")
        print("Recent rolls (newest first):")
        for i, (die1, die2, total) in enumerate(reversed(self.roll_history)):
            doubles_mark = " (DOUBLES!)" if die1 == die2 else ""
            print(f"{len(self.roll_history)-i}. [{die1}] [{die2}] = {total}{doubles_mark}")
    
    def target_mode(self):
        """Target number mode - try to roll a specific pair"""
        target_die1 = random.randint(1, 6)
        target_die2 = random.randint(1, 6)
        target_total = target_die1 + target_die2
        
        print(f"\n=== TARGET MODE ===")
        print(f"Target: [{target_die1}] [{target_die2}] = {target_total}")
        print("Try to roll this exact combination!")
        
        attempts = 0
        while True:
            choice = input("\nRoll dice? (y/n/q to quit mode): ").lower()
            if choice == 'y':
                attempts += 1
                die1, die2, roll_total = self.roll_dice()
                print(f"Roll {attempts}: [{die1}] [{die2}] = {roll_total}")
                
                if (die1 == target_die1 and die2 == target_die2) or (die1 == target_die2 and die2 == target_die1):
                    print(f"🎉 SUCCESS! You hit the target in {attempts} attempts!")
                    break
                else:
                    print("Not quite! Try again.")
            elif choice == 'n' or choice == 'q':
                print(f"Giving up after {attempts} attempts.")
                break
            else:
                print("Invalid choice! Use y/n/q")
    
    def yahtzee_mode(self):
        """Yahtzee-style scoring with two dice"""
        print("\n=== YAHTZEE MODE ===")
        print("Roll for these combinations:")
        print("- Doubles (both dice same): 10 points")
        print("- Sum of 7: 5 points") 
        print("- Sum of 2 or 12: 15 points")
        print("- Any other sum: 1 point")
        
        score = 0
        rounds = 0
        
        while True:
            choice = input(f"\nCurrent score: {score} | Roll dice? (y/n/q to quit mode): ").lower()
            if choice == 'y':
                rounds += 1
                die1, die2, roll_total = self.roll_dice()
                print(f"Round {rounds}: [{die1}] [{die2}] = {roll_total}")
                
                # Calculate points
                points = 0
                if die1 == die2:  # Doubles
                    points = 10
                    print(f"DOUBLES! +{points} points")
                elif roll_total == 7:  # Lucky 7
                    points = 5
                    print(f"Lucky 7! +{points} points")
                elif roll_total == 2 or roll_total == 12:  # Snake eyes or boxcars
                    points = 15
                    special = "Snake Eyes" if roll_total == 2 else "Boxcars"
                    print(f"{special}! +{points} points")
                else:
                    points = 1
                    print(f"+{points} point")
                
                score += points
                
            elif choice == 'n' or choice == 'q':
                if rounds > 0:
                    avg_score = score / rounds
                    print(f"Final score: {score} points in {rounds} rounds (avg: {avg_score:.1f} per round)")
                break
            else:
                print("Invalid choice! Use y/n/q")

def main():
    game = DiceGame()
    
    print("🎲 Welcome to the Enhanced Dice Game! 🎲")
    
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Free roll")
        print("2. Target mode")
        print("3. Yahtzee mode")
        print("4. View statistics")
        print("5. View roll history")
        print("6. Quit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            # Free roll mode
            roll_choice = input("Roll the dice? (y/n): ").lower()
            if roll_choice == 'y':
                die1, die2, roll_total = game.roll_dice()
                doubles_text = " - DOUBLES!" if die1 == die2 else ""
                print(f"[{die1}] [{die2}] = {roll_total}{doubles_text}")
            elif roll_choice == 'n':
                continue
            else:
                print("Invalid choice!")
                
        elif choice == '2':
            game.target_mode()
            
        elif choice == '3':
            game.yahtzee_mode()
            
        elif choice == '4':
            game.show_statistics()
            
        elif choice == '5':
            game.show_history()
            
        elif choice == '6':
            print("Thanks for playing!")
            break
            
        else:
            print("Invalid choice! Please choose 1-6.")

if __name__ == "__main__":
    main()
