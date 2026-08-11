# WHILE LOOP = EXECUTE SOME CODE WHILE SOME CONDITION REMAINS TRUE

# name = input("Enter your name : ")

# while name == "":
#     print("You did not enter your name")
#     name = input("enter your name : ")
 
# # print(f"Hello {name}")

# food = input("Enter your favourite food (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter your favourite food (q to quit): ")

# print("SEE YOU SOON BRO!")

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not Valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"You are Player {num}")