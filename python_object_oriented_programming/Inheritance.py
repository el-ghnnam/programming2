# --------------------------------------------------
# --- Object Oriented Programming => Inheritance ---
# --------------------------------------------------

# class Car:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(f'{self.name} is Created From Base Class with price are {self.price}')
#
#     def model(self):
#         print('model method from base class')
#
#
# class Model(Car):  # Derived Class
#     def __init__(self, name, price, rank):
#         # Car.__init__(self, name, price)   # OR You Can Use super()
#         super().__init__(name, price)
#         # self.name = name
#         self.price = price + 50000
#         self.rank = rank
#         print(f"{self.name} is Created From Derived Class with price are {self.price} With a {self.rank} Rank")
#
#     def test(self):
#         print("Car are Tested for a 10000 Km ")
#
#
# model_1 = Model('Toyota', 250000, 10.0)
# model_1.model()
# model_1.test()


# more examples on Inheritance
class Animal:
    alive = True

    def eat(self):
        print('This animal is eating')

    def sleep(self):
        print('This animal ia sleeping')

class Rabbit(Animal):  # Rabbit is The child class and The Animal is The Parent class
    def eating(self):
        print('This animal is eat carrot')

class Fish(Animal):
    pass

class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.eating()