import random

def generate_number(low, high):
    return random.randint(low, high)

def check_guess(guess, target):
    if guess < target:
        return "higher"
    elif guess > target:
        return "lower"
    else:
        return "correct"
def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        return 1, 50
    elif choice == "2":
        return 1, 100
    elif choice == "3":
        return 1, 200
    else:
        print("Invalid choice, defaulting to Medium (1-100).")
        return 1, 100


def play_game(best_attempts):
    low, high = choose_difficulty()
    target = generate_number(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}. Try to guess it!")

    while True:
        guess_input = input("Your guess: ")

        if not guess_input.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess_input)
        attempts += 1
        result = check_guess(guess, target)

        if result == "higher":
            print("Higher! Try again.")
        elif result == "lower":
            print("Lower! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            if best_attempts is None or attempts < best_attempts:
                best_attempts = attempts
                print("New best score!")
            break

    return best_attempts


def main():
    best_attempts = None

    while True:
        best_attempts = play_game(best_attempts)

        if best_attempts is not None:
            print(f"Best score so far: {best_attempts} attempts")

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


main()