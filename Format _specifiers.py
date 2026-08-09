# FORMAT SPECFIERS = {:flags} format a value based on what flags are 
#                     are inserted


price1 = 4675.2254
price2 = -9870.34
price3 = 1400.43

# print(f"Price 1 one is ${price1:.3f}") # NUMBER AFTER POINT IN DECIMAL
# print(f"Price 2 one is ${price2:.3f}")
# print(f"Price 3 one is ${price3:.3f}")

# print(f"Price 1 one is ${price1:10}") # FORMATS SPACES
# print(f"Price 2 one is ${price2:10}")
# print(f"Price 3 one is ${price3:10}")

# print(f"Price 1 one is ${price1:010}") # FORMAT SPACES WITH 0
# print(f"Price 2 one is ${price2:010}")
# print(f"Price 3 one is ${price3:010}")

# print(f"Price 1 one is ${price1:>10}") # RIGHT JUSTIFY
# print(f"Price 2 one is ${price2:>10}")
# print(f"Price 3 one is ${price3:>10}")

# print(f"Price 1 one is ${price1:<10}") # LEFT JUSTIFY
# print(f"Price 2 one is ${price2:<10}")
# print(f"Price 3 one is ${price3:<10}")

# print(f"Price 1 one is ${price1:^10}") # CENTRALISED
# print(f"Price 2 one is ${price2:^10}")
# print(f"Price 3 one is ${price3:^10}")

# print(f"Price 1 one is ${price1:+}") # SHOW PLUS SIGN IF ANY POSITIVE NUMBER
# print(f"Price 2 one is ${price2:+}")
# print(f"Price 3 one is ${price3:+}")

# print(f"Price 1 one is ${price1: }") # SPACES FOR SIGN
# print(f"Price 2 one is ${price2: }")
# print(f"Price 3 one is ${price3: }")

# print(f"Price 1 one is ${price1:,}") # COMMA FOR THOUSAND PLACE
# print(f"Price 2 one is ${price2:,}")
# print(f"Price 3 one is ${price3:,}")

print(f"Price 1 one is ${price1:+,.2f}") # COMMA FOR THOUSAND PLACE & plus sign for positive number & and 2 munbers after point or decimal dot
print(f"Price 2 one is ${price2:+,.2f}")
print(f"Price 3 one is ${price3:+,.2f}")