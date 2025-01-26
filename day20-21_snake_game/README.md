# Snake Game

A classic Snake game built using Python's `turtle` graphics library.

## Features
- Control the snake using the arrow keys.
- The snake grows when it eats food.
- The score increases each time food is eaten.
- The game ends if the snake hits the screen boundary or bites itself.

## Requirements
- Python 3.x installed on your machine.
- `turtle` library (which comes pre-installed with Python).

## Setup
1. Make sure you have Python installed (version 3.x).
2. No need to install external libraries as `turtle` comes with Python by default.

## File Structure
- `main.py`: The main game file where the game logic is executed.
- `my_game_screen.py`: Defines the `GameScreen` class that controls the game window.
- `food.py`: Defines the `Food` class that handles food logic.
- `snake.py`: Defines the `Snake` class that controls the snake behavior.
- `scoreboard.py`: Defines the `Scoreboard` class that displays the score.

## Running the Game
To play the game, simply run the `main.py` file:
```bash
python main.py
