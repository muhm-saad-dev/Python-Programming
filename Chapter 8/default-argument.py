def greet(name, ending = "Thank You"):
    print(f'Hello {name}')
    print(ending)
    return "Done"

a = greet("saad", "hello back")
print(a)
a = greet("rohaan")
print(a)