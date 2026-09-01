words = ["Donkey", "bad", "ganda"]

with open("doc.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))

with open("doc.txt", "w") as f:
    f.write(content)