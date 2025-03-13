#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range (2,number - 1):
       if number % i == 0:
         is_prime = False
    if is_prime == True : 
      print("Это простое число")
    else:
      print("Это не простое число")

         
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
