class Fruit:
    # parameterized constructor
    def __init__(self, name, color):
        print("This is parametrized constructor")
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)

# creating object of the class
# this will invoke parameterized constructor
obj = Fruit("Apple", "red")
# Output This is parametrized constructor

# calling the instance method using the object
obj.show()
# Output Fruit is Apple and Color is red