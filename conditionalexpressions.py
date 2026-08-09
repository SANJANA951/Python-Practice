# CONDITIONAL EXPRESSION = A one-line shortcut for if-else statement (ternary operator)
#                          Print or assign one of two values based on condition
#                          X if conditon else Y

num = 547

a = 8
b = 9

age = 19

temp = -1

user_role = "admin binod"

# print("Positive" if num > 0 else "Negative")

# result = "EVEN" if num % 2 == 0 else "ODD"

# max_num = a if a > b else b

# min_num = a if a < b else b

# status = "ADULT" if age >= 18 else "KID"

# weather = "COLD" if temp < 28 else "HOT"

access_role = "Full access" if user_role == "admin" else "Limited access"

print(access_role)