import random
import math


lower = int(input("Enter starting number"))
upper = int(input("Enter ending number"))

x = random.randint(lower,upper)

total_chance = math.ceil(math.log(upper - lower + 1,2))

print(f"\nYou have only, {total_chance} chances to guess the number\n")

count = 0
flag = False

while count < total_chance :
    count += 1
    
    guess = int(input("Your guessed number is : "))
    
    if(x == guess):
        print(f"Congratulation you did it in {count} try")
        flag = True
        break
        
    elif x > guess :
        print ("your guess is too small")
    elif x < guess:
        print("Your guess is too high")
        
if not flag :
    print("the number is %d " %x)
    print("better luck next time")
    

