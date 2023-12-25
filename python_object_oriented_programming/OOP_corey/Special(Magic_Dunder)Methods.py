class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, fname, lname, pay):  # self => refers to instance variable name
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = f"{fname}.{lname}@gmail.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return self.fname + ' ' + self.lname

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):     # __repr__ meant to be unambiguous presentation of the object(instance)
        return f'Employee({self.fname}, {self.lname}, {self.pay})'

    def __str__(self):      # __str__ meant to be a more readable representation of an object(instance)
        return f'{self.full_name()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())

#^ test __init__ method
emp1 = Employee('Ahmed', 'Ghnnam', 5000)  #* once I wirte 'Employee => class name' the init method are called.
emp2 = Employee('Maram', 'Ahmed', 6000)


#^ test __str__, __repr__ methods
# print(repr(emp1))    #~ equal to print(emp1.__repr__())   ==  print(emp1)
# print(str(emp1))     #~ equal to print(emp1.__str__())    ==  pritn(emp1)




#! Note this
print(4 + 3)            #~ equal to # print(int.__add__(4, 3))
print('ah' + 'med')     #~ equal to # print(str.__add__('ah', 'med'))
print(len('Ahmed'))     #~ equal to # print('Ahmed'.__len__())

print('-' * 50)

#^ test __add__, __len__ methods
# print(emp1 + emp2)        #~ equal print(emp1.__add__(emp2))  # self=emp1, other=emp2
# print(emp1.__len__())     #~ equal to print(len(emp1.full_name()))