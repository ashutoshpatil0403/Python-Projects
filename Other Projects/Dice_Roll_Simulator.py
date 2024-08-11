# Dice roll simulator
# The goal is to create a program that will simulate the roll of dice.

# Topics: random module, looping, and if-else

import random 
while True:     
     print('''\n 1. roll the dice           \n 2. exit     ''')    
     user = int(input("what you want to do ::"))     
     if user==1:         
        number = random.randint(1,6)         
        print("Dice Number ::",number)     
     else:         
        break
