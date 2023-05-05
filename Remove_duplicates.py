data = []
count = 10

while (count > 0):
    user_input = str(input("Enter any number of your choice: "))
    data.append(user_input)
    count = count - 1
print (data)
def remove_duplicates(data):
    newlist = []
    search = set()
    for i in data:
        if i not in search:
            newlist.append(i)
            search.add(i)
    print('\n\t', newlist)
remove_duplicates(data)