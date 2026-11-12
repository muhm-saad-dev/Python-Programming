try:
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")