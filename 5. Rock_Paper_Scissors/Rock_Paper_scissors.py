rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


list =[rock,paper,scissors]

position =input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
number=int(position)

if(number >=3 or number <0):
    print("You typed an invalid number, You lose!!")
else:
    user=list[number]
    print (user)

    print("Computer choose: \n")
    import random
    length =len(list) 
    random_index = random.randint(0,length-1)

    computer =list[random_index]
    print(computer)

    if(user==rock and  computer ==scissors):
        print("you Win !!")
    elif(user==scissors and computer == paper):
        print("you Win !!")
    elif(user==paper and computer == rock):
        print("you Win!!")
    elif(user==computer):
     print("Tie!!")
    else:
     print("you lose!")

    print("The game is over, Play again ??")