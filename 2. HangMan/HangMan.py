#import Hangman_Art
lives = 6

import random
from Hangman_Words import word_list
chosen_word = random.choice(word_list)
length = len(chosen_word)


display = []
for i in range(length):
    display+="_"

from Hangman_Art import logo, stages
print(logo)
print(f" ".join(display))
print(f"Random_word:{chosen_word}")

end_of_the_game = False

while not end_of_the_game :
    guess=input("Guess Letter: ").lower()

    if guess in display:
        print(f"you already guess {guess}")

    for position in range (length):

        letter = chosen_word[position]
        if letter == guess:
            display[position]=guess

    if  guess not in chosen_word:
        print(f"your guessed {guess} not present in the word, so you lose a life.")
        lives-=1
        if lives <=0:
            end_of_the_game=True
            print("you lose!!")

    print(f" ".join(display))

    if "_" not in display:
        end_of_the_game=True
        print("You win!!")
        break

    print(stages[lives])

