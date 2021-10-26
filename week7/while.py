# Example 7

import random


def main():
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")
    print()

    # Prepare a string that the input function will show to
    # the user during the first iteration of the while loop.
    prompt = "Please enter an integer between 1 and 100: "

    # Get a random integer between 1 and 100.
    answer = random.randint(1, 100)

    guess = -1
    attempts = 0

    while guess != answer:
        # Get a guess from the user.
        guess = int(input(prompt))
        attempts += 1

        # Compare the user's guess to the answer.
        if guess < answer:
            guide = "low"
        elif guess > answer:
            guide = "high"

        # Prepare a string that the input function will show to
        # the user during the next iteration of the while loop.
        prompt = f"{guess} is too {guide}. Please enter another integer: "

    print()
    print(f"{guess} is correct!")
    print(f"You used {attempts} guesses to guess the number.")


# Call main to start this program.
if __name__ == "__main__":
    main()