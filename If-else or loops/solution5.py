import random
def number_guessing_game():
    target_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts and not guessed_correctly:
        attempts += 1
        remaining = max_attempts - attempts

        try:
            guess = int(
                input(
                    f"Attempt {attempts}/{max_attempts} - Enter your guess: "
                )
            )
        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")
            attempts -= 1  # Do not penalize attempt count for invalid input
            continue

        if guess == target_number:
            guessed_correctly = True
            print(
                f"\nCongratulations! You guessed the number {target_number} in {attempts} attempt(s)!"
            )
            break
        elif guess > target_number:
            print("Too High!")
        else:
            print("Too Low!")

        if remaining > 0:
            print(f"Attempts remaining: {remaining}\n")

    # If the user exhausts all attempts without guessing correctly
    if not guessed_correctly:
        print(f"\nGame Over! You've run out of attempts.")
        print(f"The correct number was: {target_number}")


if __name__ == "__main__":
    number_guessing_game()