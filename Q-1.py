class Programmer:
    company = "Microsoft"
    language = "Python"
    salary = 1200000
    def __init__(self, name,  salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    

p = Programmer("Harry", 1300000, "Software Engineer")
    
print(p.company, p.name,  p.role, p.salary,p.language)

r = Programmer("Rohan", 1500000, " Senior Software Engineer")
    
print(r.company, r.name,  r.role, r.salary,r.language)

