# STRING EXERCISE

user_name = input("Enter your user name: ")

if len(user_name) > 12:
    print("User name not be more than 12 character's")

if user_name.find(" ") >0:
    print("The user name must not contain spaces") 


if user_name.isalpha() > 0:
    print("The username must not contain digits")
else:
    print(f"WELCOME {user_name}")