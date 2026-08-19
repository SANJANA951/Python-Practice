words = ["donkey", "mouse", "stuupid", "criminal", "mad", "bad", "coward", "elephant", "cat"]

with open("prince.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(words))

with open("prince.txt", "w") as f:
    f.write(content)
    