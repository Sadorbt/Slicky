# import re
# string = input("Enter the string :")
# count = 0
# string = string.lower()
# for i in string:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#             count+=1
#     elif i == "x":
#           break
# print("Bye homie")
# print('Total vowels are :' + str(count))

def countVowels():
    # declare count
    count = 0
    # Take a string from input    
    string = input("Enter the string :")

    # check if string contains vowels
    for i in string:
        if(i.lower() in 'aeiou'):
            # if string contains vowels, count the number of vowels
            count +=1

    # print the count of vowels
    print('Total vowels are :' + str(count))

    # check if string contains x
    if('x' in string.lower()):
        print("Bye homie")
    else:
        # if there is no X, recall the function
        countVowels() 

countVowels()