class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")

harry = Employee()
# harry.language = "Javascript" # This is a instance attribute
harry.greet()
harry.getinfo()
#Employee.getinfo(harry)