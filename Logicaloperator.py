# LOGICAL OPERATOR

# or =  ATLEATS ONE STATMENT MUST BE TRUE

temp = -69
is_sunny = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is not cancelled!!")

# #AND = BOTH CONDITIONS MUST BE TRUE

# temp = 45
# is_sunny = True

# if temp > 35 and is_sunny:
#     print("It's Sun's Day")

# else:
#     print("It's not Sun's Day")

# NOT = INVERTS THE CONDITION ( NOT TRUE OR NOT FALSE)

if temp  < 28 and  not is_sunny:
    print("It's Cold Day")
    

else:
    print("It's  Sun's Day")
    print("BUT THE TEMP IS VERY LOW")
