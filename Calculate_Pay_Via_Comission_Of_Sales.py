sales = int(input("What's your total sales for the month? "))
amount = int(input("How much advance have you taken this month? "))
advance = amount - 2000
def calculatepay():
 if sales<=10000:
  salary = (sales * 0.1) - advance
 elif sales>10000 and sales<=14999:
  salary = (sales * 0.12) - advance
 elif sales>=15000 and  sales <=17999:
  salary = (sales * 0.14) - advance
 elif sales>=18000 and sales <= 21999:
   salary = (sales * 0.16) - advance
 elif sales>=22000:
  salary = (sales * 0.18) - advance
  if salary < 0:
   print("Please reimburse the company")
  else:
   print (salary)
 calculatepay()
