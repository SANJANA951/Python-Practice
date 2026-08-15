a = {
     "marks": 100,
     "Harry": 97,
     "Prince": 35,
     "Sachin": 85,
}

#print(a.items())
#print(a.keys())
#print(a.values())
#a.update({"marks": "Virat", "Rohit": 45})
#print(a)

print(a.get("Prince2"))# Prints None
print(a["Prince2"]) # Returns an error