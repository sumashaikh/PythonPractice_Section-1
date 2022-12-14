class Vehicle:
	def __init__(self,name,milenge,capacity):
		self.name=name
		self.milenge=milenge
		self.capacity=capacity

	def fare(self):
	    return self.capacity*100

class Bus(Vehicle):
	pass

School_bus=Bus("volvo",108,18)

print("total bus fare is",School_bus.fare())	
