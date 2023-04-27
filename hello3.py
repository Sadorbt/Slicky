
S_C = {
         "Abia" : "Umuahia",  "Adamawa" : "Yola",   "Akwa_Ibom" : "Uyo",
         "Anambra" : "Awka",  "Bauchi" : "Bauchi",   "Bayelsa" : "Yenagoa",
         "Benue" : "Makurdi",  "Borno" : "Maiduguri",  "Cross_River" : "Calabar",
          "Delta" : "Asaba",    "Ebonyi" : "Abakaliki",   "Edo" : "Benin_City",
         "Ekiti" : "Ado_Ekiti",   "Enugu" : "Enugu",   "Gombe" : "Gombe", 
           "Imo" : "Owerri",    "Jigawa" : "Dutse",    "Kaduna" : "Kaduna",
          "Kano" : "Kano",     "Katsina" : "Katsina",    "Kebbi" : "Birnin_Kebbi",
           "Kwara" : "Ilorin",     "Lagos" : "Ikeja",      "Nasarawa" : "Lafia",
            "Niger" : "Minna",    "Ogun" : "Abeokuta",     "Ondo" : "Akure",
            "Osun" : "Oshogbo",    "Oyo" : "Ibadan",     "Plateau" : "Jos",
         "Rivers" : "Port_Harcourt",  "Sokoto" : "Sokoto",   "Taraba" : "Jalingo ",
          "Yobe" : "Damaturu",    "Zamfara" : "Gusau",     "Abuja" : "FCT",
            }		

states = S_C.keys()
capitals = S_C.values()

for states, capitals in S_C.items():
   print(states,capitals)

user = input("Which state are inquiring about? ")

capital = S_C[user.capitalize()]
print(capital)
 