class Circle:
     
    pi=3.14
 
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        
        print("Area of circle:",self.pi*self.radius*self.radius)

class Rectangle:

    def __init__(self,length,width):

    	self.length = length
    	self.width = width

    def calculate_area(self):
    	print("Area of Rectangle : ",self.length*self.width)


cir=Circle(5)
rect=Rectangle(10,5)
cir.calculate_area()


rect.calculate_area()