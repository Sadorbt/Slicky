import math
print (math.pi)
length = 50
print ("input a number within 1 to 50 for your pi decimal")
a = ("Not a valid number. Enter within the appropriate range or press q to exist")
c = ("You have entered q to exit. Goodbye!")
k = 1
while k:
    try:
        n = int(input("How many decimal places do you want:- "))
        if n == "q":
            print (c)
        else:
            print(a)

        b ='{:.' + str (n) + 'f}'
        if n > 50 or n < 0:
            print (a)
        else:
            print('PI =' + b.format(math.pi))

        w = input("Very neat..., right? press y to run it again. Press q to exist:- " )
        if w == "y" or w == "Y":
            k=1
        elif w == "q" or w == "Q":
            k = 0
            print(c)
        else:
            print("Not a valid entry. Auto-restarted. input a number within 1 to 50 for your pi decimal. Press q anytime to exit." )
            k = 1
        
    except ValueError:
        print(a)
        
       