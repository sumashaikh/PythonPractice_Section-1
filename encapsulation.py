class Employee:

	def __init__(self,name,salary):

		self.name=name
		self._salary=salary

	def show(self):
		print("name is",self.name."and salary is",self._salary)

E=Employee("jesa",40000)
E.printname()
E.(E.name)
E.(E.printname())
print(E.salary)