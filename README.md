# Group3-Educational-Game-Project

## Description
This repository contains the code for the 'Educational Snake Game' application. The application builds on the concept of the traditional snake game, by including educational features like solving simple arithmetic equations and unscrambling the given words. At the end of the game, player is allowed to save their names with the latest score, to keep a track on their progress.

Our main aim of building this application is to help children 'Learn Through Play'.

Pygame library is used for building the gaming application. The user is given an option to play a 'Number Game' or a 'Word Game'. Following are the instructions and descriptions of how each game works.

### Number Game

* Initially the game starts with a score of 0 and maximum lives of snake as 3 lives.
* There is an arithmetic equation that is displayed on top of the screen.
* Answer to the equation is displayed as one of the random numbers in the screen.
* If the correct number is picked up by the snake: 
1. The score increases by 1.
2. A new arithmetic equation is displayed on top of the screen.
3. New random numbers along with the answer to the equation is displayed for the snake to pick.

* If a wrong answer is picked up by the snake:
1. Total number of lives is decreases by 1. 
2. Another random number is generated and displayed along with the remaining numbers.

* If the snake hits itself or the edges of the screen, the total number of lives decreases by 1.
* Game is over when the snake loses all 3 lives.
* Note: the player can then write their name to be added with the score to the database. 
* Due to time constraints, this was not implemented fully.

### Word Game

* Initially the game starts with a score of 0 and maximum lives of snake as 3 lives.
* The word to be guessed is displayed with blank spaces at the top of the game.
* All the letters of the word to be guessed are scattered on the screen for the snake to pick them up in the correct order.
* As the snake picks up each letter one by one, this appears correspondingly on top of the screen.
* Once all letters are picked up the game checks if the word formed is correct.
* Player's score increases by 1 when the correct word is formed, otherwise loses a life.
* A new word with the corresponding letters are displayed on the screen.
* If the snake hits itself or the edges of the screen, the total number of lives decreases by 1.
* Game is over when the snake loses all 3 lives.
* Note: the player can then write their name to be added with the score to the database. 
* Due to time constraints, this was not implemented fully.

## Installation

The application can be run by running the python file `edu_snake_game.py` in the main project folder.

All test cases for the application can be run in the terminal using the following command from the main project folder:
```
python -m unittest discover tests
```

## Credits

This application was built as part of a project while completing the CFGDegree-Software Specialisation course.

### Team Members
* Alisha Musamabik
* Timea Kiraly
* Sian Tipping
* Jayashree Karthikeyan
* Lima Jamal
