# OOP Exercise 1: Create a Class with instance attributes
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# modelX = Vehicle(240, 18)
# print(modelX.max_speed, modelX.mileage)
#
# print("_" * 40)
# # OOP Exercise 2: Create a Vehicle class without any variables and methods
# class Vehicle:
#     pass
print("_" * 40)
# # OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 180, 12)
# print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
print("_" * 40)
# OOP Exercise 4: Class Inheritance
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     # assign default value to capacity
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)
#
# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.seating_capacity())
print("_" * 40)
# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# class Vehicle:
#     # Class attribute
#     color = "White"
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
#
# car = Car("Audi Q5", 240, 18)
# print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
print("_" * 40)
