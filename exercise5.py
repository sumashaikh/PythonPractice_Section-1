class Vehicle:
	color = "white"
	def __init__(self,name,max_speed,milenge):
		self.name=name
		self.max_speed=max_speed
		self.milenge=milenge

class Bus(Vehicle):
    pass

class car(Vehicle):
	pass

School_bus=Bus("School Volovo",180,12)
emply_car=car("Audi",20,18)

print("color:",School_bus.color,"vehicle name",School_bus.name,"speed",School_bus.max_speed,"milenge",School_bus.milenge)	
print("color:",emply_car.color,"vehicle name",emply_car.name,"speed",emply_car.max_speed,"milenge",emply_car.milenge)	



    				    		