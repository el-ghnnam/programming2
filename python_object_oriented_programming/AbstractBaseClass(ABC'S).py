# ----------------------------------------------------------------
# -- Object Oriented Programming => Abstract Base Class (ABC'S) --
# ----------------------------------------------------------------
# - Class Called Abstract Class If It Has One Or More Abstract Methods
# - abc Module In Python Provides Infrastructure For Defining Custom Absstract Base Class
# - By Adding @abstractmethod Decorator On The Methods
# -@abstractmethod doesn't do anything so when we implement a abstract method we should use a pass keyword.
# - ABCMeta Class Is A Metaclass Used For Defining Abstract Base Class
# ----------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod


class programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):
        pass

# classes that inherit from A abstract base class should have the same methods that exist in this class.


class python(programming):
    def has_oop(self):
        return 'Yes'


class pascal(programming):
    def has_oop(self):
        return 'No'


language_one = python()
print(python.has_oop(language_one))
