class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print("Name is ", self.name, "and salary is", self.__salary)

# Outside class
E = Employee("Jessa", 40000)
E.PrintName()
print(E.name)
print(E.PrintName())
print(E.__salary)
# AttributeError: 'Employee' object has no attribute '__salary'