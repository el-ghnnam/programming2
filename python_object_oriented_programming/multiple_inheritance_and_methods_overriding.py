# ----------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance ---
# ----------------------------------------------------------
# Multiple Inheritance

class Base_one :
    def __init__(self, name):
        self.name = name
        print(f'Base_one And name is {self.name}')
    
class Base_two :
    def __init__(self, name):
        self.name = name
        print(f'Base_two And name is {self.name}')

class Derived_class(Base_two, Base_one):
    def __init__(self, name,):
        super().__init__(name)
        print('Hello From Derived Class.')

Derived_one = Derived_class('ahmed')

class One:
    pass

class Two(One):       # class Three Have Access To All Methods in class One.
    pass

class Three(Two):     # class Three Have Access To All Methods in class Two and class One.
    pass

print("_" * 40)

# class Prey:
#     def __init__(self):
#         print('This animal is flees')
#     def flee(self):
#         print('This is animal')
#
# class Predator:
#     def __init__(self):
#         print('This animal is hunting')
#     def hunt(self):
#         print('This is animal')
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
# fish_1 = Fish()
# rabbit.flee()rabbit = Rabbit()
# # hawk = Hawk()
# hawk.hunt()
# fish_1.hunt()
# print(Fish.mro())     # mor => Method Resolution Order
print("_" * 40)

# Overriding # if you have the same of methods in the parent class and child class,
# and you call this method from the child class, the output will be the implement of this method in child class
# class Animal:
#     def eat(self):
#         print('This animal is eating')
#
# class Shark(Animal):
#     def eat(self):
#         print("This animal eating a Fishes")
# animal1 = Shark()
# animal1.eat()

print("_" * 40)

# multilevel inheritance
# class Superclass:
#     def derived(self):
#         print('Hello from Superclass')
# class Level1(Superclass):
#     def derived1(self):
#         print('Hello from derived1')
# class Level2(Level1):
#     def derived2(self):
#         print('Hello from derived2')
#
# derive1 = Level2()
#
# derive1.derived2()
# derive1.derived1()
# derive1.derived()
print("_" * 40)


