class vehicle:

     def __init__(self,name,max_speed,milenge):
         self.name = name
         self.max_speed=max_speed
         self.milenge = milenge

     def seating_capacity(self,capacity):
         return f"the seating capacity of a {self.name} is {capacity} passengers"      

class Bus(vehicle):
     def seating_capacity(self,capacity=50):
         return super().seating_capacity(capacity=50)

School_bus=Bus("School Volovo",180,12)

print(School_bus.seating_capacity())                  