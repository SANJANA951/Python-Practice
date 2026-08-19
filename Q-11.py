
import os

with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write


if os.path.exists("old.txt"):
    os.remove("old.txt")
else:
    print("File not found")

