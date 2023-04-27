# Write a program that asks the user f0r a number n and 
# gives them the possibility to choose between computing
# the sum and computing the product.
user_input = int(input("input a number of your choice here "))
a = list(range(1 , user_input))
print (a)
def multiplication(a) :
    product = 1
    for i in a :
        product = product * i
    return product
addition = sum(a)
user_input2 = input("Will you like to sum up the number or find the product? ( + / x )")
if user_input2 == "+":
    print(addition)
elif user_input2 == "x":
    print(multiplication(a))

