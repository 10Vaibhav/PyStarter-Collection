# NATO Phonetic Alphabet Converter

This project provides a simple Python script that converts words into their NATO phonetic alphabet equivalents.

## Description

The NATO Phonetic Alphabet Converter reads from a CSV file containing the NATO phonetic alphabet and allows users to input words, which are then converted to their corresponding NATO phonetic code words.

## Features

- Reads NATO phonetic alphabet data from a CSV file
- Converts user input to uppercase
- Provides phonetic code words for each letter in the input
- Handles errors for non-alphabetic characters

## Requirements

- Python 3.x
- pandas library

## Files

- `main.py`: The main Python script
- `nato_phonetic_alphabet.csv`: CSV file containing the NATO phonetic alphabet

## How it Works

1. The script reads the NATO phonetic alphabet from the CSV file using pandas.
2. It creates a dictionary mapping each letter to its phonetic code word.
3. User input is converted to uppercase.
4. The script then looks up each letter in the dictionary and creates a list of corresponding phonetic code words.
5. If a non-alphabetic character is entered, the script catches the KeyError and prompts the user to try again.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.

