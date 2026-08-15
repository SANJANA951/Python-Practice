def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 1
b = 5
c = 3

print(greatest(a, b ,c))

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is {inch_to_cms(n)}")

def multiply(n):
    for i in range(1, 11):
      print(f"{n} X {i} = {n*i}")

multiply(6)      
