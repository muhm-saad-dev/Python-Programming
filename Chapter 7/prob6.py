# using for loop
print('using for loop')

n = int(input('Enter a number for Factorial: '))

fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)


# using while loop
print('using while loop')

n = int(input('Enter a number for Factorial: '))
fact1 = 1
j = 1
while(j<=n):
    fact1 *= j
    j+=1
print(fact1)