#Data Types

#String
"Hello"

#Integer
123

#Float
3.14159

#Boolean
True
False

#Type Errors
num_char = len(input("What is your name?"))
print("Your name has " + str(num_char) + " characters.")

#Type Checking
print(type(num_char))

#Type Conversion
str()
int()
float()
bool()

# Maths Operations
3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3

# PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)
# ()
# **
# * /
# + -

print(3 * (3 + 3) / 3 - 3)

#Rounding Numbers
round(4.6666666666)

#Floor division
print(9 // 4)

#Shorthand Operators
# a += 2  short for a = a + 2
# -=
# *=
# /=


#f-Strings
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")