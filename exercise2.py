#  


# 2nd way to slove this 

# num = int(input("Enter the number:"))
# check = int(input("Enter the numver divided by:"))
# if num % 4 == 0:
#     print(num,"it is multiply by 4")
# elif num % 2 == 0:
#     print(num,"it is even number") 
# else:
#     print(num,"it is odd number")
# if num % check == 0:
#     print(num,"divided evenly by ", check)
# else:
#     print(num,"id not divided evenly by", check)

num = int (input("Enter a number:"))
check = int(input("Enter the number divide by: "))
if num % 4 == 0:
    print(num,"it is multiply by 4")
elif num % 2 == 0:
    print(num,"it is even number")
else:
    print(num,"it is odd number")
if num % check == 0:
    print(num,"divided by evenly into num",check)
else:
    print(num,"is not divided by evenly",check)                
