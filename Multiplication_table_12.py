# Write a program that prints a multiplication table
# for any number up to 12
user_input = int(input("Pick a number and the multiplication table will be printed for you"))
def my_function(user_input):
  print ("multiplicatioon Table of ", user_input)
for i in range(1 , 13):
    print (f"{user_input} X {i} = {user_input*i}")
my_function(user_input)
