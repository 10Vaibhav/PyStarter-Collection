def caesar(start_text,shift_amount,cipher_direction):

    shift_i=shift_amount%len(alphabet)
    end_text=""

    if cipher_direction=="decode":
        shift_i*=-1
    for char in start_text:
        if char in alphabet:
          position=alphabet.index(char)
          new_position=position+shift_i
          new_letter=alphabet[new_position]
          end_text+=new_letter
        else:
            end_text+=char

    print(f"The {cipher_direction} message is: {end_text}")


import Art_cipher
print(Art_cipher.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shouldGo=True
while shouldGo:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

    answer=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if answer=="no":
        shouldGo=False
        print("Good Bye.")

