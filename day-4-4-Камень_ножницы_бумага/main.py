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
choice_player = input("Сделайте ваш выбор: 0-камень,1-ножницы,2-бумага ")
print ("Ваш выбор - ", (choice_player))

import random
choice_computer = random.randint (0, 3)
print ("Выбор компьютера - ", (choice_computer))


 






