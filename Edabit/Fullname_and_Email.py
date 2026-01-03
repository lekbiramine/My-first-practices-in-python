class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = f"{self.firstname} {self.lastname}"
        self.email = f"{self.firstname}.{self.lastname}@company.com".lower()

    
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname)
print(emp_2.email)
print(emp_3.firstname)