a = [ 14, 5, 55, 35, 40, 60]

def divisible5(n):
    if(n%5 == 0):
        return True
    return False


f = list(filter(divisible5, a))
print(f)