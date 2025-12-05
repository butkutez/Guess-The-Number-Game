import random


# Step 1: Function to generate a random number
def generate_random_number():
    return random.randint(1, 100)  # Random number between 1 and 100


# Step 2: Function to manage one round of play
def play_round(target_number):
    try:
        guess = int(input("Enter your guess (1-100): "))
    except ValueError:
        print("Please enter a valid number.")
        return False  # Invalid input does not count as a correct guess

    if guess < 1 or guess > 100:
        print("Your guess must be between 1 and 100.")
        return False

    if guess == target_number:
        return True
    elif guess < target_number:
        print("Too low!")
    else:
        print("Too high!")
    return False


# Step 3: Main game loop
def guess_the_number():

    player_name = input("Enter your name: ")

    target_number = generate_random_number()
    max_rounds = 10

    for round_number in range(1, max_rounds + 1):
        print(f"\nRound {round_number} of {max_rounds}")
        if play_round(target_number):
            print(f"{player_name}, you guessed the correct number in {round_number} rounds.")
            break
    else:
        print(f"{player_name}, you failed, try again!")


# Start the game
guess_the_number()

