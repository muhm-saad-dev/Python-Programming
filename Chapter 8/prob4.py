def nsum(n):
    if(n == 1 or n == 0):
        return 0
    return n + nsum(n-1)

n = int(input('Enter a number: '))

print(nsum(n))