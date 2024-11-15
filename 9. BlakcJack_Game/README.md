# Blackjack Game

This is a Python implementation of the classic casino card game Blackjack (also known as 21).

## Description

This Blackjack game allows players to play against a computer dealer. The objective is to get a hand value as close to 21 as possible without going over. Face cards are worth 10, Aces can be 1 or 11, and all other cards are worth their face value.

## Features

- Random card dealing
- Score calculation with special handling for Aces
- Computer dealer AI
- Option to hit or stand
- Automatic detection of Blackjack (21 with two cards)
- Clear console interface

## Files

1. `Black_jack.py`: The main game logic
2. `Art.py`: ASCII art for the game logo

## How to Play

1. Run `Black_jack.py`
2. You will be dealt two cards, and the dealer will show one card
3. Choose to 'hit' (get another card) or 'stand' (keep your current hand)
4. Try to get as close to 21 as possible without going over
5. After you stand, the dealer will play their hand
6. The higher score wins, but going over 21 means an automatic loss

## Game Rules

- Blackjack (an Ace with a 10-value card) beats all other hands
- Aces are worth 11 unless that would put the hand over 21, then they're worth 1

## Requirements

- Python 3.x

## Contributing

Contributions, issues, and feature requests are welcome.
