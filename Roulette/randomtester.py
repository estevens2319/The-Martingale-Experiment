# A test to see how random the random generator is. 


import os
import random

os.system('cls' if os.name == 'nt' else 'clear')

print("Random Tester")

numTests = 10000000
num = 0
for i in range(numTests):
    ran = random.random()
    if(ran <= .474):
        num+=1
print(num)