

import random

test_seed = int (input ("Create a seed number:  ")) 
random.seed (test_seed) 
random_integer = random.randint (0, 1)
print(random_integer)
print(test_seed)

if random_integer == 1:
   print("Решка")
else:  
   print("Орел")

