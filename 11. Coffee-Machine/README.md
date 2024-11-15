# Coffee Machine Simulator

A Python-based simulation of a coffee machine that allows users to order drinks, manage resources, and handle transactions.

## Description

This Coffee Machine Simulator is a command-line program that mimics the functionality of a real coffee machine. It offers a menu of drinks, manages resources, processes coin payments, and serves virtual coffee drinks.

## Features

- Menu with three drink options: espresso, latte, and cappuccino
- Resource management (water, milk, coffee)
- Coin processing (quarters, dimes, nickles, pennies)
- Transaction handling
- Ability to check machine status with a "report" command
- Option to turn off the machine

## Files

- `coffe_Machine.py`: The main program file containing the coffee machine logic
- `Data.py`: Contains the menu and resource data
- `Coffee+Machine+Program+Requirements.docx`: Detailed requirements for the program

## Commands

- Type `espresso`, `latte`, or `cappuccino` to order a drink
- Type `report` to view the current resource levels and money collected
- Type `off` to turn off the coffee machine and exit the program

## Program Flow

1. The program prompts the user for their choice
2. If ordering a drink:
- Checks if there are sufficient resources
- Prompts for coin insertion
- Processes the transaction
- Dispenses the drink and updates resources
3. If `report` is entered, it displays the current status
4. If `off` is entered, the program terminates

## Requirements

- Python 3.x

## Contributing

Contributions to improve the Coffee Machine Simulator are welcome!
