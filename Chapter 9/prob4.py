word = "Donkey"

with open("doc.txt") as f:
    content = f.read()

newContent = content.replace(word, "######")

with open("doc.txt", "w") as f:
    f.write(newContent)