numerals = {"I" : "1", 'II' : "2", 'III' : "3", "IV" : "4", 'V' : "5",
'VI' : "6", "VII" : "7", 'VIII' : "8", "IX" : "9", "X" : "10",
"XI" : "11", "XII" : "12", "XIII" : "13",  "XIV": "14", "XV" : "15",
"XVI" : "16",	'XVII' : "17", 'XVIII' : "18",  'XIX' : "19", 'XX' : "20", "Q" : "Goodbye"}
roman = numerals.keys()
decimal = numerals.values()
user_input = str(input("Input a roman numeral within the range 0 - 21 :- "))
for roman, decimal in numerals.items():
    pass
while (user_input != "Q"):
    user_input = str(input("Input a roman numeral within the range 0 - 21 :- "))
    roman = numerals[user_input]
    print(roman)




    
   



