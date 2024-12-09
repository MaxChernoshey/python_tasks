# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("год високосный")
    else:
      print("год не високосный")
  else:
    print("год високосный")
else:
  print("год не високосный")
  