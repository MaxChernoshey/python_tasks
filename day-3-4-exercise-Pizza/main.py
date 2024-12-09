# 🚨 Don't change the code below 👇
print("Добро пожаловать в заказчик пиццы на пайтоне!")
size = input("Какой размер пиццы вы хотите? S, M, or L ")
add_pepperoni = input("Хотите перерони? Y or N ")
extra_cheese = input("Хотите дополнительный сыр? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S":
  bill += 15
  
elif size == "M":
  bill += 20
  
elif size == "L":
  bill += 25
print({bill})

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  elif size == "M":
    bill += 3
  elif size == "L":
    bill += 3    
if extra_cheese == "Y":
  bill += 1
    
print(f"Your final bill is $ {bill}")