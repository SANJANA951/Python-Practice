from functools import reduce 
l = [11,3345,5544,34,5656,6686,675,4444]


def greater(a, b):
    if(a>b):
        return a 
    return b


print(reduce(greater, l))