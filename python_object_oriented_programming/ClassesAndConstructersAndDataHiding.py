
# Constructor(__init__) is a special method in python
# Special methods are automatically called during object creation


# class Name:
#     name = ''
#     age = 0
# name1 = Name()
# # name1.name = 'Ahmed'
# # name1.age = 19
# print(f'{name1.name} is {name1.age} years old')


# class Name:
#     def __init__(self, name='Maram', age=12):
#         self.name = name
#         self.age = age
#
#
# name1 = Name()
# print(f'{name1.name} is {name1.age} years old')

print("_" * 40)

# --- Data_Hiding(Encapsulation) -----------------------------------------

#---Restrict Access To The Data Stored in Attributes and Methods
# Public
#---Every Attribute and Method That We Used So Far Is Public
#---Attributes and Methods Can Be Modified and Run From Everywhere
#---Inside Our Outside The Class
# Protected
#---Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
#---Attributes and Methods Prefixed With One Underscore_
# Private
#---Attributes and Methods Can Be Accessed From Within The Class Or Object Only
#---Attributes Cannot Be Modified From Outside The Class
#---Attributes and Methods Prefixed With Two Underscores
# ------------   attribute == properties == variables   --------------
# Encapsulation is one of the key features of object-oriented programming.
# Encapsulation refers to the bundling of attributes and methods inside a single class.
# It prevents outer classes from accessing and changing attributes and methods of a class.
# This also helps to achieve data hiding.
# In Python, we denote private attributes using underscore as the prefix i.e single _ or double __

# class Member:
#     def __init__(self, name):
#         self.name = name     # Public attribute
#
# one = Member('Ahmed')
# print(one.name)
# one.name = "Maram"
# print(one.name)
print("_" * 40)

# class Member:
#     def __init__(self, name):
#         self.name = name     # protected attribute
#
# one = Member('Ahmed')
# print(one._name)
# one._name = "Maram"
# print(one._name)
print("_" * 40)
# class Member:
#     def __init__(self, name):
#         self.__name = name     # private attribute
#     def say_hello(self):
#         print(f' Hello {self.__name}')
#
# one = Member('Ahmed')
# one.say_hello()
# # print(one.__name)   # Error
# # one.__name = "Maram"
# # print(one.__name)   # Error
# print(one._Member__name)
print("_" * 40)


# class Computer:
#     def __init__(self):
#         self.__maxprice = 900  # private attribute
#
#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))
#
#     def setMaxPrice(self, price):
#         self.__maxprice = price
#
# comp1 = Computer()
# comp1.sell()
# comp1.__maxprice = 1000    #  Doesn't change still '900'
# comp1.sell()
# comp1.setMaxPrice(1000)    # only way to change the price for the private attributes
# comp1.sell()
print("_" * 40)