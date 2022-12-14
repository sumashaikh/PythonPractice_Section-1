class Test:
    # Constructor - non parameterized
    def __init__(self):
        print("This is non parametrized constructor")

    def show(self, name):
        print("Hello", name)

# creating object of the class
t = Test()
# Output:This is non parametrized constructor

# calling the instance method
t.show("Jessa")
# Output Hello Jessa