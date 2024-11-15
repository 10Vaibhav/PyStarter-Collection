# Hangman Game

A classic Hangman game implemented in Python. Players try to guess a hidden word, letter by letter, before running out of lives.

## Description

This Hangman game randomly selects a word from a predefined list and challenges the player to guess it. The game features ASCII art for visual representation of the hangman and provides feedback on correct and incorrect guesses.

## Features

- Random word selection from a large word list
- ASCII art representation of the hangman
- Visual feedback on correct guesses and remaining lives
- Input validation and duplicate guess checking

## Files

- `HangMan.py`: Main game script
- `Hangman_Art.py`: Contains ASCII art for the logo and hangman stages
- `Hangman_Words.py`: List of words used in the game

## Requirements

- Python 3.x

##  Follow the on-screen prompts to play the game:
1. The game will display the hidden word as underscores.
2. Guess a letter by typing it and pressing Enter.
3. The game will update the display, showing correctly guessed letters.
4. Continue guessing until you solve the word or run out of lives.

## Game Rules

- You start with 6 lives.
- Each incorrect guess reduces your lives by 1.
- Guess all letters in the word before running out of lives to win.
- The game ends when you guess the word correctly or run out of lives.

## Contributing

Contributions, issues, and feature requests are welcome.
