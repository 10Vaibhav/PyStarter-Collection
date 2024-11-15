import Art,os,random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def check_score(user,computer,user_sum,computer_sum):
    if user_sum<computer_sum:
        print(f"    You lose")
    elif user_sum==computer_sum:
        print(f"    Draw")
    elif computer_sum==21:
        print(f"    Lose,opponent has Blackjack!!")
    elif computer_sum>21:
        print(f"    you win")
    else:
        print(f"    you win")


def BlackJack():
    shouldGo=True
    user_list=[]
    computer_list=[]
    while shouldGo:
        length=2
        user_cards_sum=0
        computer_cards_sum=0

        while length>0:
            U_item=random.choice(cards)
            user_list.append(U_item)
            C_item=random.choice(cards)
            computer_list.append(C_item)
            user_cards_sum+=U_item
            computer_cards_sum+=C_item
            length-=1

        if user_cards_sum>=21:
            user_list.remove(11)
            user_list.append(1)

        print(f"    your cards: {user_list}, current score : {user_cards_sum}")
        print(f"    Computer's first hand: {computer_list[0]}")

        again=True
        while again:
            user2=input("Type 'y' to get another card or 'n' to pass : ")
            if user2=='y':
                add_item=random.choice(cards)
                user_list.append(add_item)
                user_cards_sum+=add_item

                if user_cards_sum>21:
                    print(f"    your final hand: {user_list}, final score: {user_cards_sum} ")
                    print(f"    computer's final hand: {computer_list}, final score: {computer_cards_sum}")
                    print(f"    you went over. You lose")
                    again=False
                    break
                elif user_cards_sum==21:
                    print(f"    your cards: {user_list}, final score : {user_cards_sum}")
                    print(f"    Computer's final hand: {computer_list}, final score: {computer_cards_sum}")
                    print(" win with a BlackJack.")
                    again=False
                    break
                else:
                    if computer_cards_sum!=0 and computer_cards_sum <17:
                        C_item=random.choice(cards)
                        computer_list.append(C_item)
                        computer_cards_sum+=C_item
                print(f"    your cards: {user_list}, current score : {user_cards_sum}")
                print(f"    Computer's first hand: {computer_list[0]}")
            else:
                print(f"    your final hand: {user_list}, final score: {user_cards_sum} ")
                print(f"    computer's final hand: {computer_list}, final score: {computer_cards_sum}")
                check_score(user=user_list,computer=computer_list,user_sum=user_cards_sum,computer_sum=computer_cards_sum)
                again=False
                break

        result=input("Do you want to play BlackJack?, Type 'y' or 'n':  ")
        shouldGo=False
        break
    if result=='y':
        os.system('cls')
        print(Art.logo)
        BlackJack()
    else:
        print("Okk.Have a nice day")

answer=input("Do you want to play BlackJack?, Type 'y' or 'n':  ")
if answer=='y':
    print(Art.logo)
    BlackJack()
else:
    print("Okk,Have a nice day.")






