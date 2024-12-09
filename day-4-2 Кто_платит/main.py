

import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(",")
# 🚨 Don't change the code above 👆
print(names)
print(namesAsCSV)

# способ 1
num_members = len(names)
print(num_members)
random_choice = random.randint(0, num_members - 1)
names_who_pays = names[random_choice]
print("Будет платить -", names_who_pays)

#способ 2
random.shuffle(names)
random_number = random.choice(names)

print("Будет платить -", random_number)






