print( "welcome to rollercoaster!")
height = int(input("what is your height in cm?\n"))
bill =0


if height >=  120:
  print("you can ride the rollercoaster!")
  age = int(input("what is your age?\n"))

  if age < 12:
    bill=5
    print("Child ticket is $5.")
  elif age <= 18 :
    bill=7
    print("Youth ticket is $7.")
  elif  age >= 45 and age <55:
      bill=0
      print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill=12
    print("Adult ticket is $12.")

  want_photo = input("If you to take a photo? Y or N\n")
  if want_photo == "Y":
    bill +=3

  print(f"your total bill is  ${bill}.")
else:

  print("sorry, you have to grow taller before you can ride. ")