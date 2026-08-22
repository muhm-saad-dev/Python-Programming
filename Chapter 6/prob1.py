a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
c = int(input('Enter number c: '))
d = int(input('Enter number d: '))

if(a>b and a>c and a>d):
    print(f'a = {a} is greater number')
elif(b>a and b>c and b>d):
    print(f'b = {b} is greater number')
elif(c>a and c>b and c>d):
    print(f'c = {c} is greater number')
elif(d>a and d>b and d>c):
    print(f'd = {d} is greater number')
else:
    print('none is greater ')