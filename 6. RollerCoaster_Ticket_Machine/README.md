# Rollercoaster Ticket Machine

A simple Python program that simulates a ticket machine for a rollercoaster ride, calculating ticket prices based on age and height.

## Description

This program determines whether a person can ride the rollercoaster based on their height, and then calculates the ticket price based on their age. It also offers an option for a photo and adjusts the price accordingly.

## Features

- Height check for ride eligibility
- Age-based pricing
- Special free ride offer for a specific age group
- Optional photo add-on

## How It Works

1. The program asks for the user's height in centimeters.
2. If the height is at least 120 cm, the user can ride; otherwise, they are told they need to grow taller.
3. For eligible riders, the program asks for their age.
4. Ticket price is determined based on age:
   - Under 12: $5 (Child ticket)
   - 12-18: $7 (Youth ticket)
   - 45-55: Free ride
   - All others: $12 (Adult ticket)
5. The user is asked if they want a photo (costs an additional $3).
6. The total bill is calculated and displayed.

## Example Interaction
welcome to rollercoaster!
what is your height in cm?
150
you can ride the rollercoaster!
what is your age?
25
Adult ticket is $12.
If you to take a photo? Y or N
Y
your total bill is  $15.
