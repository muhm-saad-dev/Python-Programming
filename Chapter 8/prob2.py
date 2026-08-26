def f2c(f):
    return 5*(f-32)/9

f = int(input('Enter a temprature in fahrenhight: '))
a = f2c(f)
print(f'{round(a, 2)} °C')