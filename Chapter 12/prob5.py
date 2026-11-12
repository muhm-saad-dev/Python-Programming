n = int(input("Enter a number for display in list: "))

table = [i*n for i in range(1, 11)]
with open ("tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")
