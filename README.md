# Guess-The-Number-Game
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Property_Price_Predictor](https://i.pinimg.com/1200x/d0/cb/6a/d0cb6aeabb07ebf5420eb6b45998bc21.jpg)](https://in.pinterest.com/pin/550354016936114257/)  
*Image source: [Peakpx](https://in.pinterest.com/pin/550354016936114257/)*

## Project Description

This is a classic Guess the Number game implemented in Python. The objective of the game is for the player to guess a randomly generated secret number between 1 and 100 within a maximum limit of 10 rounds.

After each guess, the game provides hints,telling the player if their guess was "Too high!" or "Too low!", to help them narrow down the range. This project is a simple, command-line application focusing on core programming fundamentals.

## Core Implementation
This project utilizes several fundamental Python programming concepts:

- Functions (Modular game components)

- Loops (for loop for game rounds)

- Conditionals (if/elif/else for guess comparison and input validation)

- Input Handling (input() and try/except for validation)

- Randomization (random.randint)

## Getting started

### Installation
You only need to have Python 3.x installed on your system. No external libraries are required, as the game uses the standard random module.

**1. Clone the project**

```
cmd git clone https://github.com/butkutez/Guess-The-Number-Game.git
```
**2. Navigate to the project folder**
```
cd Guess-The-Number-Game
```

**3. Run the main scraper**
````
python game.py
````

## Repo structure

```
GUESS_THE_NUMBER_GAME
├── README.md
└── game.py
```

## Usage (How to Play)

- **Start the Game**: Run the Python script using python game.py.

- **Enter Your Name**: The game will first prompt you to enter your name.

- **The Guessing Loop**:

    - The game starts a loop, announcing the current round number (e.g., Round 1 of 10).

    - You are prompted: Enter your guess (1-100):

    - Enter a number and press Enter.

- **Receive Feedback**:

    - If your guess is correct, the game congratulates you and ends immediately.

    - If your guess is incorrect, the game prints "Too high!" or "Too low!" and proceeds to the next round.

    - If you enter an invalid number (non-numeric, or outside the 1-100 range), the round does not count, and you are prompted again.

- **Game End**: The game ends when either:

    - You guess the number correctly (breaks the loop).

    - You reach the maximum limit of 10 rounds (triggers the else block of the main game loop).

## The Core Functionality

The game logic is organized into three simple and distinct functions:

- **generate_random_number()**: Creates and returns the secret number, an integer between 1 and 100.

- **play_round(target_number)**: Manages a single turn. It takes user input, validates it (numeric and range checks), compares the guess to the target_number, prints the appropriate hint ("Too high!"/"Too low!"), and returns True if the guess is correct, otherwise False.

- **guess_the_number()**: This is the main function that runs the game. It gets the player's name, sets the target_number, executes the 10-round loop, calls play_round() on each iteration, and announces the final result (win or loss).

## Timeline

This project was completed over **1 days**, adhering to a focused rapid development schedule.

## Personal Situation
This project was completed as a **personal initiative** to practice and solidify several core Python programming concepts in a practical, self-contained application.

**Connect** with me on [LinkedIn](https://www.linkedin.com/in/zivile-butkute/).



[![Gaming GIF](https://media1.tenor.com/m/xDic2PfW958AAAAC/victory-winning.gif)](https://tenor.com/en-GB/view/victory-winning-yes-gif-14139223485814601631)  
*Image source: [tenor](https://tenor.com/en-GB/view/victory-winning-yes-gif-14139223485814601631)*