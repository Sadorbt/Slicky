n_number = int (input ("Input a number here: "))
n = range(1, n_number+1)

def my_function(n):
    for i in n :
        if (i%3 == 0 or i%5 == 0):
            print(" FizzBuzz ")
        elif i%3==0:
            print(" Fizz ")
        elif i%5==0:
            print(" Buzz ")
        else:
            print(i)
    
my_function(n)
