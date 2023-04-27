# Write a program tat asks the user their name and greets them with their name. 
# The program should ask the user for a number "n" and print the sum of the 
# numbers 1 to n. Only multiples of 3 and 5 should be considered in the sum, 
# e.g 3, 5, 6, 9, 10 e.t.c


user_name = input ("Enter your name here: ")
print ( 'Hello   '   +  (user_name)  )
n_number = int (input ("Input a number here: "))
def my_function(n_number):
 total_sum = 0
 for i in range( 1, n_number) :
    if (i%3 == 0 or i%5 == 0) :
       total_sum += i
 print(total_sum)
my_function(n_number)
