def reverser():
    user_input = str(input('Type in a sentence stating your name:- '))
    element = user_input.split(' ')
    reverse = ' '.join(reversed(element))
    print(reverse)
reverser()