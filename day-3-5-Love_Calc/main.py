# 🚨 Don't change the code below 👇
#print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


t = name1.count('t')
print(f" T occurs { t } times")
r = name1.count('r')
print(f" R occurs { r } times")
u = name1.count('u')
print(f" U occurs { u } times")
e = name1.count('r')
print(f" E occurs { e } times")
Total1 = t + r + u + e
print(f" Total1 = { Total1 }")

l = name2.count('l')
print(f" L occurs { l } times")
o = name2.count('o')
print(f" O occurs { o } times")
v = name2.count('v')
print(f" V occurs { v } times")
e = name2.count('e')
print(f" E occurs { e } times")
Total2 = l + o + v + e
print(f" Total2 = { Total2 }")
Love_Score = int(str(Total1) + str(Total2))
print(f" Love Score = { Love_Score }")
#print(f" Love Score = {Total1}{Total2}")

#Love_Score = int(input({Total1}{Total2}))

if Love_Score < 10 or Love_Score > 90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score >= 40 and Love_Score <= 50:
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"Your score is {Love_Score}")