#CH 9 zyBooks - Classes

### Challenge 9.2.2 Declaring a class ###
# ''' Your solution goes here '''
# class PatientData:
#     def __init__(self, height_inches=0, weight_pounds=0):
#         self.height_inches = height_inches
#         self.weight_pounds = weight_pounds
#The code above was all I had to do, code below was given.
# patient = PatientData()
# print('Patient data (before):', end=' ')
# print(f'{patient.height_inches} in,', end=' ')
# print(f'{patient.weight_pounds} lbs')

# patient.height_inches = int(input())
# patient.weight_pounds = int(input())

# print('Patient data (after):', end=' ')
# print(f'{patient.height_inches} in,', end=' ')
# print(f'{patient.weight_pounds} lbs')



### Challenge 9.2.3 Access a classes attributes ###
# class InventoryTag:
#     def __init__(self):
#         self.item_id = 0
#         self.quantity_remaining = 0

# red_sweater = InventoryTag()
# red_sweater.item_id = int(input())
# red_sweater.quantity_remaining = int(input())

# #All i had to do was print the attributes, item_id and quantity_remaining.
# #Note: the object was red_sweater and the class was InventoryTag
# ''' Your solution goes here '''
# print(f'ID: {red_sweater.item_id}')
# print(f'Qty: {red_sweater.quantity_remaining}')



### 9.3.1 Instance Methods ###
#I think this is a good example of Instance Methods
# class Person:
#    def __init__(self):
#       self.first_name = ''
#       self.last_name = ''

#    def get_full_name(self):
#       return self.first_name + '_' + self.last_name
#This function? formats the output of the two prints. I believe its called a class method.

# a_first_name = 'May'
# another_first_name = 'Max'
# a_last_name = 'Stark'
# another_last_name = 'Rogers'

# person1 = Person()
# person2 = Person()

# person2.first_name = a_first_name
# person1.first_name = another_first_name
# person2.last_name = a_last_name
# person1.last_name = another_last_name

# print(f'You are {person1.get_full_name()}')
# print(f'I am {person2.get_full_name()}')

### 9.3.2 Define an Instance Method
# class PersonInfo:
#     def __init__(self):
#         self.num_kids = 0

#     # FIXME: Write inc_num_kids(self)
#Adding the num=1 was what got me. After that we increment by num.

#     ''' Your solution goes here '''
#     def inc_num_kids(self, num=1):
#         self.num_kids += num

# person1 = PersonInfo()
# print(f'Kids: {person1.num_kids}')
# person1.inc_num_kids()
# print(f'New baby, kids now: {person1.num_kids}')

### Challenge 9.6.2 Defining a Class Constructor ###
#Write a constructor with parameters self, num_mins and num_messages.
#num_mins and num_messages should have a default value of 0.
# class PhonePlan:
#     # FIXME add constructor
#     def __init__(self, num_mins=0, num_messages=0):
#         self.num_mins = num_mins
#         self.num_messages = num_messages
#     ''' Your solution goes here '''

# #This was given:
#     def print_plan(self):
#         print(f'Mins: {self.num_mins}', end=' ')
#         print(f'Messages: {self.num_messages}')

# my_plan = PhonePlan(int(input()), int(input()))
# dads_plan = PhonePlan()
# moms_plan = PhonePlan(int(input()))

# print('My plan...', end=' ')
# my_plan.print_plan()
# print('Dad\'s plan...', end=' ')
# dads_plan.print_plan()
# print('Mom\'s plan...', end= ' ')
# moms_plan.print_plan()

### 9.8 Class Customization Example ###
# Below we use the __str__() method to define how the class, Toy is printed.
# class Toy:
#     def __init__(self, name, price, min_age):
#         self.name = name
#         self.price = price
#         self.min_age = min_age

#Note how we don't use print() here:
#     def __str__(self):
#         return (f'{self.name} costs only ${self.price:.2f}. Not for children under {self.min_age}!')

#now we print
# truck = Toy('Monster Truck XX', 14.99, 5)
# print(truck)

#Operatior Overloading
# Rich comparison method	  Overloaded operator
# __lt__(self, other)	     less than (<)
# __le__(self, other)	     less than or equal to (<=)
# __gt__(self, other)	     greater than (>)
# __ge__(self, other)	     greater than or equal to (>=)
# __eq__(self, other)	     equal to (==)
# __ne__(self, other)	     not equal to (!=)

#9.9 More Overloading Operators
# Method	                   Description
# __add__(self, other)	     Add (+)
# __sub__(self, other)	     Subtract (-)
# __mul__(self, other)	     Multiply (*)
# __truediv__(self, other)	 Divide (/)
# __floordiv__(self, other)  Floored division (//)
# __mod__(self, other)	     Modulus (%)
# __pow__(self, other)	     Exponentiation (**)
# __and__(self, other)	     "and" logical operator
# __or__(self, other)	       "or"    logical operator
# __abs__(self)	             Absolute value (abs())
# __int__(self)	             Convert to integer (int())
# __float__(self)	           Convert to floating point (float())
