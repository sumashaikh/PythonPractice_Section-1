class Employee:
    def __init__(self, id, name):
        # instance variable
        self.id = id
        self.name = name
    
    # instance method
    def info(self):
        print("Employee ID is ", self.id, "and name is", self.name)

    # instance method 
    def department(self):
        print("Employee of IT department")

emp = Employee(10112, "Harry", )
emp.info()
# Output Employee ID is 10112 and name is Harry

emp.department()
# Output Employee of IT department