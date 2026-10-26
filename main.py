import random

# Simplified configuration dictionary name
DIFFICULTIES = {
    "Easy": 10,
    "Medium": 5,
    "Hard": 3
}

def print_welcome_message():
    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

def get_difficulty_choice(prompt_text: str) -> str:
    print(prompt_text)
    menu_index = 1
    for level_name, max_chances in DIFFICULTIES.items():
        print(f"{menu_index}. {level_name} ({max_chances} chances)")
        menu_index += 1
    print("4. Quit")
    return input("Enter your choice: ").lower().strip()

def run_game_engine():
    while True:
        print_welcome_message()
        user_input = get_difficulty_choice("Please select the difficulty level:")
        
        if user_input in ["quit", "4"]:
            print("\nThanks for playing! Goodbye.")
            break

        level_names_list = list(DIFFICULTIES.keys())
        
        try:
            selected_index = int(user_input) - 1
            if selected_index not in range(0, 3):
                raise ValueError
            chosen_level = level_names_list[selected_index]
        except ValueError:
            print("\nInvalid selection. Please try again.")
            continue 
        else:
            allowed_chances = DIFFICULTIES[chosen_level]
            print(f"""
Great! You have selected the {chosen_level} difficulty level.
You have {allowed_chances} chances to guess the correct number.
Let's start the game!
""")
        
        secret_number = random.randint(1, 100)
        
        for attempt_count in range(1, allowed_chances + 1):
            try:
                player_guess = int(input("Enter your guess: ").strip())
                if player_guess not in range(1, 101):
                    print("Guess must be between 1 and 100.")
                    continue
            except ValueError:
                print("Invalid guess number. Please enter an integer.")
                continue

            if player_guess == secret_number:
                print(f"Congratulations! You guessed the correct number in {attempt_count} attempts.")
                break
            elif secret_number < player_guess:
                print(f"Incorrect! The number is less than {player_guess}.\n")
            else:
                print(f"Incorrect! The number is greater than {player_guess}.\n")
        else:
            print(f"Game Over! You ran out of chances. The number was {secret_number}.\n")

if __name__ == "__main__":
    run_game_engine()
