import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# keys = data.letter.to_list()
# values = data.code.to_list()
#
# dictor = {keys[i]: values[i] for i in range(0, 24)}

dictor = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# ** Method 1 ** :
# go = True
#
# while go:
#     try:
#         word = input("Enter a word: ").upper()
#         phonetic = [dictor[select] for select in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#
#     else:
#         print(phonetic)
#         go = False

# ** Method 2 ** :
def generate():
    try:
        word = input("Enter a word: ").upper()
        phonetic = [dictor[select] for select in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()

    else:
        print(phonetic)
        go = False


generate()
