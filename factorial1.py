0
def factorial(n):
    if n == 0:      # base case
        return 1
    return n * factorial(n-1)  # recursive case

n = int(input("Enter a number: "))
print(factorial(n))