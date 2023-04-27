data = []

while True:
    user_input = input("Enter a character: ")
    data.append( user_input)
    if  user_input.casefold() == "x":
     break
for element in data:
  print(data)
print(len(data))
print(" , , , , , , , , , , , , , , , , , , , , , , , , ,")

data2 = []

while True:
    user_input2 = (input("Will you like to swap any two indexes? (yes/no)"))
    data2.append(user_input2)
    if user_input2.casefold() == "yes":
     break
for element in data2:
     print ("Choose any two number out of the following(0,1,2,3,4,5)")
    
first_number =int(input("first "))
second_number =int(input("second ")) 
print("Alright, you'll your result in a minute")
def swappositions(data, first_number, second_number):
   temp_first_number = data[first_number]
   temp_second_number = data[second_number]
   data[first_number] = temp_second_number
   data[second_number] = temp_first_number
   return data

print(swappositions(data, first_number, second_number))
