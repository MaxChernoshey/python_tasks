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

#Write your code below this line 👇
choice_player = int(input("Сделайте ваш выбор: 0-камень,1-ножницы,2-бумага "))
print ("Ваш выбор - ", (choice_player))
if choice_player == 0 :
  print (rock)
elif choice_player == 1 :
  print (scissors)
elif choice_player == 2 :
  print (paper)
else:
  print ("Вы ввели неверное число, техническое поражение")

import random
choice_computer = random.randint (0, 2)
print ("Выбор компьютера - ", (choice_computer))

if choice_computer == 0 :
  print (rock)
elif choice_computer == 1 :
  print (scissors)
else:
  print (paper)

if choice_player == 0 :
    if choice_computer == 0 :
     print ("Ничья")
    elif choice_computer == 1 :  
     print ("Компьютер проиграл")
    else:     
     print ("Компьютер выиграл")
elif choice_player == 1 :
    if choice_computer == 0 :
     print ("Компьютер выиграл")
    elif choice_computer == 1 :  
     print ("Ничья")
    else:     
     print ("Компьютер проиграл")
elif choice_player == 2 :
    if choice_computer == 0 :
     print ("Компьютер проиграл")
    elif choice_computer == 1 :  
     print ("Компьютер выиграл")
    else:     
     print ("Ничья")
else:
  print ("Вы ввели неверное число")
 






