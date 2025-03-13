
import random

from arts import stages

from words import word_list

from arts import logo
print(logo)
# word_list = ["aardvark", "baboon", "camel"]
random.shuffle(word_list)
random_word = random.choice(word_list)
dlina_slova = len(random_word)
lives = 6
print(random_word)
print("длина слова -",dlina_slova)

display_word = []
for n in range(0, len(random_word)):
     display_word.append("_")
print(display_word)


# for n in range(dlina_slova):   
end_of_game = False
while not end_of_game:
  print("остаток жизней",lives + 1)  
  user_letter = input("What is your letter? \n")

  k = 0
  for i in random_word:
    if i == user_letter:
      display_word[k] = (user_letter)
    k = k + 1 
  
  if user_letter not in random_word:
  # if l == 0:
      print("Нет такой буквы")
      print(stages[lives])
      lives = lives - 1
      if lives < 0:
        print("You lose.")
        end_of_game = True  

  
  print(display_word)

  if "_" not in display_word:
    end_of_game = True
    print("You win")

