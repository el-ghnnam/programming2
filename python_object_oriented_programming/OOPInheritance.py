# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

class Food :
    def __init__(self, Name, cost):
        self.name = Name
        self.cost = cost
        print (f'{self.name} Is Created From Main Class.') 

    def eat(self):
        print ('Eat Is Created From Base Class.')



class Apple(Food):
    def __init__(self, name, cost, amount):
        Food.__init__(self, name, cost)
        # super().__init__(name, cost)
        self.name = name
        self.cost = cost + 15
        self.amount = amount

        print (f'{self.name} Is Created From Derived Class And The Cost Is {self.cost} And The Amount Is {self.amount}.')

    def get_from_tree(self):
        print('Get Apple From Tree In The Derived Class.')



# food_one = Food('Pizza')

food_two = Apple('Checken', 125, '4K')
# food_two.eat()
# food_two.get_from_tree()