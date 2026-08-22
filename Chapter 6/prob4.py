name = input('Enter your username under 10 characters: ')
a = len(name)
if(a < 10):
    print('Yes : this is under 10 characters')
elif( a >= 10):
    print('No : there are more characters then 10')