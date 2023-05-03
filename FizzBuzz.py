n_number = int (input ("Input a number here: "))
n = range(1, n_number+1)

def my_function(n):
    output = []
    print (output)
    for i in n :
        if (i%3 == 0 or i%5 == 0) :
            output.append(" FizzBuzz ")
        elif i%3==0:
            output.append(" Fizz ")
        elif i%5==0:
            output.append(" Buzz ")
        else:
            output.append(i)
    print (output)
    
my_function(n)