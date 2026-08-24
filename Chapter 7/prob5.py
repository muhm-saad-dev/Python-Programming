n = int(input('Enter a number for sum: '))
sum = 0
for i in range(1, n+1):
    sum += i

print(sum)


# using while loop
sum = 0
j = 0
while(j<=n):
    sum += j
    j += 1
print(sum)