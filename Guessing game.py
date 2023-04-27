import random
import math


lower = int(input("Input the lowest range number:- "))
upper = int(input("Input the highest range number:- "))
count = 0
chances = round((math.log(upper - lower + 1) *2))
random_number = random.randint(lower, upper)
print("\n\tYou've only ", chances," chances to guess the integer!")

while (chances > 0):
      print('Chances inside: ', chances)
      guess = int(input("Guess a number:- "))
      chances = chances - 1
      if random_number == guess:
            print('Congrations you did')
            break
      elif random_number > guess:
            print('You guessed too small babes!')
      else:
            print('You guessed too high Gee!')

if chances == 0:
      print("\nThe number is %d" % random_number)
      print("\tBetter Luck Next Time!")
      print("Game Over!")