with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes python is present in the content")
else:
    print("No python is not present in the content")

