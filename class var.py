class Employee:
      
      department="python"
 
      def show(self):

      	 print("department is ",self.department)

emp = Employee()

emp.show()    

print("class variables:",Employee.department)	 