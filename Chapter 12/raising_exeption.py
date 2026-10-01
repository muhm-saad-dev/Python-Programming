a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if(b == 0):
    raise ZeroDivisionError ("Second number should not be the 0")
else:
    print(f"The division a/b is {a/b}")
