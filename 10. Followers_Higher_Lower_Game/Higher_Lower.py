from Game_Data import data
import random, os, Art

length = len(data)

score = 0

initial_position1 = random.randint(0, length - 1)
currentA = initial_position1
initial_position2 = random.randint(0, length - 1)
currentB = initial_position2
location1 = 0
location2 = 0
shouldGo = True

print(Art.logo)

while shouldGo:
    print(f"Compare A: {data[currentA]['name']}, {data[currentA]['description']}, from {data[currentA]['country']}.")
    print(Art.vs)
    print(f"Against B: {data[currentB]['name']}, {data[currentB]['description']}, from {data[currentB]['country']}.")

    answer = input("who has more followers? Type 'A' or 'B': ")
    if answer == 'A':
        location1 = currentA
        location2 = currentB

    if answer == 'B':
        location1 = currentB
        location2 = currentA

    if data[location1]['follower_count'] > data[location2]['follower_count']:
        score += 1
        currentA = currentB
        old = currentB
        currentB = random.randint(0, length - 1)

        if currentB == old:
            currentB = random.randint(0, length - 1)

        os.system('cls')
        print(Art.logo)
        print(f"You're right! Current score: {score}")

    else:
        os.system('cls')
        print(Art.logo)
        print(f"Sorry, that's wrong. Final Score: {score}")
        shouldGo = False
