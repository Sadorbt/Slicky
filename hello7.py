# Write a function that takes date of birth as and
# parameter and returns the user's age
from datetime import date

date_of_birth = int(input("Which years were you born:- "))
todays_date = date.today().strftime("%Y")
print("Your current age is ", int(todays_date) - date_of_birth)