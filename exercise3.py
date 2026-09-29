# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# for x in a:
#     if x<5:
#         print(x)
#combine the challeng 1 and 2  
# print([x for x in a if x<5])        

# And here is a sample solution that solves the exercise with extra 3.
numbers = [7,31,3,6,8,5,1,2,4,15,9,10,12,14,11]
lessFnums = []
lessNnums = []
for num in numbers:
    if num < 5:
        lessFnums.append(num)
        lessFnums.sort()
print(lessFnums)
print()

# Ask the user for a number and return a list that contains only elements from the original 
num  = int(input("Enter a numbber:"))
for n in numbers:
    if n < num:
        lessNnums.append(num)
        lessNnums.sort()
print(lessNnums)
print()        