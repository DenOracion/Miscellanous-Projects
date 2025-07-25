import re

# Common passwords list for Rule 10
common_passwords = {"password", "123456", "12345678", "qwerty", "abc123", "letmein", "111111", "123123"}

def display_current_rule(rule_number):
    """Display only the current rule the user needs to pass"""
    rules = {
        1: "Rule 1: Password must be at least 8 characters long",
        2: "Rule 2: Must include at least one uppercase letter (A-Z)",
        3: "Rule 3: Must include at least one lowercase letter (a-z)",
        4: "Rule 4: Must include at least one number (0-9)",
        5: "Rule 5: Must include at least one special character (!@#$%^&*...)",
        6: "Rule 6: Password must not contain spaces",
        7: "Rule 7: Password must start with a letter",
        8: "Rule 8: No character may be repeated 3 times in a row",
        9: "Rule 9: Password must not contain your name",
        10: "Rule 10: Password cannot be a common password"
    }
    
    print(f"\n📋 Current Challenge:")
    print(f"   {rules[rule_number]}")
    print("-" * 50)

def check_single_rule(password, username, rule_number):
    """Check only a specific rule and return True if it passes"""
    
    if rule_number == 1:
        # Rule 1: Minimum length
        return len(password) >= 8
    
    elif rule_number == 2:
        # Rule 2: At least one uppercase letter
        return bool(re.search(r'[A-Z]', password))
    
    elif rule_number == 3:
        # Rule 3: At least one lowercase letter
        return bool(re.search(r'[a-z]', password))
    
    elif rule_number == 4:
        # Rule 4: At least one digit
        return bool(re.search(r'\d', password))
    
    elif rule_number == 5:
        # Rule 5: At least one special character
        return bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|`~]', password))
    
    elif rule_number == 6:
        # Rule 6: No spaces
        return " " not in password
    
    elif rule_number == 7:
        # Rule 7: Starts with a letter
        return password and password[0].isalpha()
    
    elif rule_number == 8:
        # Rule 8: No 3 repeated characters in a row
        return not bool(re.search(r'(.)\1\1', password))
    
    elif rule_number == 9:
        # Rule 9: Cannot contain the username (case-insensitive)
        return username.lower() not in password.lower()
    
    elif rule_number == 10:
        # Rule 10: Not a common password
        return password.lower() not in common_passwords
    
    return False

def main():
    print("🔐 Welcome to The Password Game!")
    print("💡 You'll face 10 rules, one at a time. Pass each rule to advance!")
    username = input("Enter your name: ").strip()

    MAX_ATTEMPTS = 3
    current_rule = 1
    total_rules = 10

    while current_rule <= total_rules:
        attempts = 0
        
        while attempts < MAX_ATTEMPTS:
            # Show current rule
            display_current_rule(current_rule)
            
            password = input(f"Enter your password (Rule {current_rule}, Attempt {attempts + 1}/{MAX_ATTEMPTS}): ").strip()
            
            # Check if current rule passes
            if check_single_rule(password, username, current_rule):
                print(f"✅ Rule {current_rule} passed! Moving to next rule... 🎉")
                current_rule += 1
                break  # Move to next rule
            else:
                attempts += 1
                print(f"❌ Rule {current_rule} failed!")
                
                if attempts < MAX_ATTEMPTS:
                    print(f"🔁 You have {MAX_ATTEMPTS - attempts} attempts remaining for this rule.")
                else:
                    print(f"💥 You've used all {MAX_ATTEMPTS} attempts for Rule {current_rule}.")
                    restart = input("Would you like to restart from Rule 1? (y/n): ").strip().lower()
                    if restart == 'y':
                        current_rule = 1  # Reset to first rule
                        break
                    else:
                        print("Thanks for playing! 👋")
                        return

    # If this message is displayed, all rules were passed
    print("\n🎊 CONGRATULATIONS! 🎊")
    print("You've successfully passed all 10 rules!")
    print("Your password is approved! 🔐✨")

if __name__ == "__main__":
    main()
