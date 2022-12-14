my_list = list([2, 4, 6, 8, 10, 12])

# modify single item
my_list[0] = 20
print(my_list)

#modify range of items
#modify from 1st index to 4th
my_list[1:4]=[40,60,80]
print(my_list)

# modify from 3rd index to end

my_list[3:]=[80,100,120]
print(my_list)

#MODIFY ALL THE ITEMS 

my_list1=list([2,4,6,8])
# change value of all items

for i in range(len(my_list1)):
# calculate square of each number
  square=my_list1[i]*my_list1[i]
  my_list1[i]=square
print(my_list1)