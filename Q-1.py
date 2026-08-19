f = open("poems.txt")
content = f.read()

if("Twinkle" in content):
    print("the word twinkle is present in the content")

else:
    print("the word twinkle is not present in the content")


f.close()
