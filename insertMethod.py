#ADD ITEM AT THE SPECIFID POSITION IN THE LIST
# use the insert() method to add the object /item at the specified position in the list .
#the insert method accepts two parameter position and object
# insert(index,object)
my_list=list([5,8,'tom',7.50])
 
#using insert()
#insert 25 at position 2
my_list.insert(2,25)
print(my_list)

#insert nested list at the position 3
my_list.insert(3,[25,50,75])
print(my_list)

#USING EXTEND METHOD

#the extended method will accept the list of elements and add them at the end of the list .we can even add
# anothe list by using this method
my_list1=list([5,8,'tom',7.50])
my_list1.extend([25,75,100])
print(my_list1)

