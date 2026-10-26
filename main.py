import random

DIFFICULTY_LEVEL = {
    "Easy": 10,
    "Medium": 5,
    "Hard": 3
}

def display_menu():
    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

def select_level(prompt: str) -> str:
    print(prompt)
    num = 1
    for level, chances in DIFFICULTY_LEVEL.items():
        print(f"{num}. {level} ({chances} chances)")
        num += 1
    print("4. Quit")
    return input("Enter your choice: ").lower().strip()

def workflow():
    while True:
        display_menu()
        user_choice = select_level("Please select the difficulty level:")
        
        if user_choice in ["quit", "4"]:
            print("\nThanks for playing! Goodbye.")
            break

        levels_list = list(DIFFICULTY_LEVEL.keys())
        
        try:
            choice_idx = int(user_choice) - 1
            if choice_idx not in range(0, 3):
                raise ValueError
            selected_level = levels_list[choice_idx]
        except ValueError:
            print("\nInvalid selection. Please try again.")
            continue 
        else:
            chances = DIFFICULTY_LEVEL[selected_level]
            print(f"""
Great! You have selected the {selected_level} difficulty level.
You have {chances} chances to guess the correct number.
Let's start the game!
""")
        
        random_num = random.randint(1, 100)
        
        for chance in range(1, chances + 1):
            try:
                guess_number = int(input("Enter your guess: ").strip())
                if guess_number not in range(1, 101):
                    print("Guess must be between 1 and 100.")
                    continue
            except ValueError:
                print("Invalid guess number. Please enter an integer.")
                continue

            if guess_number == random_num:
                print(f"Congratulations! You guessed the correct number in {chance} attempts.")
                break
            elif random_num < guess_number:
                print(f"Incorrect! The number is less than {guess_number}.\n")
            else:
                print(f"Incorrect! The number is greater than {guess_number}.\n")
        else:
            print(f"Game Over! You ran out of chances. The number was {random_num}.\n")

if __name__ == "__main__":
    workflow()
