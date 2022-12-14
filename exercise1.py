# Create a child class Bus that will inherit all of the varibles and methods of the Vehicle class

class Vehicle:

	def __init__(self,name,max_speed,milenge):
		self.name = name
		self.max_speed = max_speed
		self.milenge = milenge
class Bus(Vehicle):
	pass

school_bus=Bus("sumayya",20,108)
print("vehicle name",school_bus.name,"speed",school_bus.max_speed,"milenge",school_bus.milenge)	