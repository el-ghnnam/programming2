# ---------------------------------------------------------
# class Author:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#     def set_auther_info(self, newname, newaddress):
#         self.name = newname
#         self.address = newaddress
#
#     def get_author_info(self):
#         return f'Author\'s name is {self.name}, Author\'s address is {self.address}'
#
#
# class Book:
#     def __init__(self, name, publisher, year, author):
#         self.name = name
#         self.publisher = publisher
#         self.year = year
#         self.author = author
#
#     def set_book_info(self, newname, publisher, year):
#         self.name = newname
#         self.publisher = publisher
#         self.year = year
#
#     def set_author_info(self, author):
#         self.author = author
#
#     def get_book_info(self):
#         return f'Tho Book for "{self.author}" Called a "{self.name}" Published By The "{self.publisher}" in year "{self.year}"'
#
#
# author1 = Author('John Doe', 'USA')
# book1 = Book('SPACE', 'HYBRID_PUBLISHERS', 1995, author1.name)
# print(book1.get_book_info())
#
# author2 = Author("Mostafa Mahmoud", "EGYPT")
# book2 = Book("من أسرار القرآن", 'NASAR_LIBRARY', 1977, author2.name)
# print(book2.get_book_info())
print("-" * 50)

# Get Area of a Circle
# class Circle:
#     def __init__(self, r):
#         self.radius = r
#
#     def get_area(self):
#         return (self.radius ** 2) * 3.14
#
#
# circle1 = Circle(5)
# print(circle1.get_area())
print("-" * 50)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_x(self, x):
#         self.x = x
#
#     def set_Y(self, y):
#         self.y = y
#
#     def set_xy(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_point(self):
#         return f'({self.x}, {self.y})'
#
#     def get_distance(self, another_x, another_y):
#         distance = (((self.x - another_x) ** 2) + ((self.y - another_y) ** 2) ** .5)
#         return f'Distance is {distance:.2f}'
#
#     def get_distance2(self, another_point):
#         distance = (((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** .5)
#         return f'Distance is {distance:.3f}'
#
#
# p1 = Point(10, 15)
# print(p1.get_distance(20, 30))
#
# p2 = Point(9, 12)
# p3 = Point(30, 40)
# print(p3.get_distance2(p2))
print("-" * 50)

# What will be the output of the following Python code?
# class test:
#     def __init__(self, a="Hello World"):
#         self.a = a
#
#     def display(self):
#         print(self.a)
#
#
# obj = test()
# obj.display()
print("_" * 40)


# class change:
#     def __init__(self, x, y, z):
#         self.sum = x + y + z
#         print('Hello Ahmed')
# number = change(1, 2, 3)
# print(number.sum)
print("_" * 40)
#
# class A:
#     def __init__(self,b):
#         self.b=b
#     def display(self):
#         print(self.b)
# obj=A("Hello")
# del obj
print("_" * 40)

# What will be the output of the following Python code?
# class test:
#     def __init__(self):
#         self.variable = 'Old'
#         self.Change(self.variable)
#     def Change(self, var):
#         var = 'New'
# obj=test()
# print(obj.variable)
print("_" * 40)
# What will be the output of the following Python code?

# class fruits:
#     def __init__(self, price):
#         self.price = price
# obj=fruits(50)
# obj.quantity=10
# obj.bags=2
# print(obj.price)
# print(obj.bags)
print("_" * 40)

# What will be the output of the following Python code?
# def add(c, k):
#     c.test = c.test + 1
#     k = k + 1
# class A:
#     def __init__(self):
#         self.test = 0
# def main():
#     Count = A()
#     k = 0
#     for i in range(0, 25):
#         add(Count, k)
#     print("Count.test=", Count.test)
#     print("k =", k)
# main()
print("_" * 40)
# What will be the output of the following Python code?

# class B(object):
#   def first(self):
#     print("First method called")
#   def second(self):
#     print("Second method called")
# ob = B()
# B.first(ob)
print("_" * 40)
# class Demo:
#     def __new__(self):
#         self.__init__(self)
#         print("Demo's __new__() invoked")
#     def __init__(self):
#         print("Demo's __init__() invoked")
# class Derived_Demo(Demo):
#     def __new__(self):
#         print("Derived_Demo's __new__() invoked")
#     def __init__(self):
#         print("Derived_Demo's __init__() invoked")
# def main():
#     obj1 = Derived_Demo()
#     obj2 = Demo()
# main()
print("_" * 40)

