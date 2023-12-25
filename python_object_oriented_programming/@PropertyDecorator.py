# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------


class Info:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f'Hello {self.name}')

    @property           # بتخليك تنادي ال ميثود من غير ما تحط الاقواس
    def CalcAgeInDays(self):
        return f'Your Age Is {self.age * 365}. '


person_one = Info('Ahmed', 19)
print(person_one.name)              # Called Property
print(person_one.age)
print(person_one.sayHello())        # Called Method
print(person_one.CalcAgeInDays)     # Called as a Property
print(person_one.CalcAgeInDays())     # error
