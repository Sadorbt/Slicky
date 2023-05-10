file = (open('divine.txt', 'r'))
read = file.readlines()
print(read)
with open ('divine.txt', 'r') as file:
    lines = [line.strip() for line in file]
for line in lines:
    tadan = (line.split())
    print (tadan)
    print("The total number of words in the paragraph is:-", len(tadan))
