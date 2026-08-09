# # PYTHON COMPUND INTEREST CALCULATOR


principle = 0
rate = 0
time = 0 

while True:
    principle = float(input("Enter the principle: "))
    if principle < 0:
        print("Principle can't be equal or less than  zero")
    else:
        break

while rate <= 0:
    rate = float(input("Enter the Rate : "))
    if rate < 0:
        print("Rate can't be equal or less than  zero")
    else:
        break

while True:
    time = int(input("Enter the Time in years: "))
    if time < 0:
        print("Time can't be equal or less than to zero")
    else:
        break

total = principle * pow((1 + rate / 100),time)

print(f"Balance after {time} Years: Rupess {total:.2f}")





