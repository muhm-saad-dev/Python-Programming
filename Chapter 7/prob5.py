# using for loop
print('Sum using for loop')
n = int(input('Enter a number for sum: '))
sum = 0
for i in range(1, n+1):
    sum += i

print(sum)


# using while loop
print('Sum using while loop')
m = int(input('Enter a number for sum: '))
sum = 0
j = 0
while(j<=m):
    sum += j
    j += 1
print(sum)