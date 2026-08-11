# TEMPERATURE CONVERTER

unit = input("Is the temperature is in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the Temperature: "))

if unit=="C":
    temp = round((temp * 1.8) + 32,1)
    print(f"The Temperature in Fahrenheit is :{temp} F")
elif unit=="F":
    temp = round((temp - 32) / 1.8,1)
    print(f"The Temperature in Celsius is :{temp} C")

   

else:
    print(f"{unit} is a invalid unit for measurement")