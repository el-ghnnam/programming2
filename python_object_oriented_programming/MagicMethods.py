# ----------------------------------------------------------
# -- Object Oriented Programming => Magic(Dunder) Methods --
# ----------------------------------------------------------
#  EveryThing In Python Is Object.
# __init__ Called Automatically When Instantiating class(When Construct A New Object).
# self.__class__ => The Class To Which A Class Instance Belong.
# __str__ Gives A Human-Readable Output Of The Object.
# __len__ Returns The Length Of The Container.
#           Call When We Use The Built-In Len() Funtction On The Object.
# ----------------------------------------------------------

class Skill:
# __init__
    def __init__(self):
        self.skills = ['Html', 'Css', 'JS']
    def __str__(self):
        return f'This is My skills => {self.skills}.'
    def __len__(self):
        return len(self.skills)


profile = Skill()
# print(profile.skills)
# print(profile.__str__())
print(profile.__len__())   #  == 3 --> ['Html', 'Css', 'JS'] 
profile.skills.append('Python')
# print(profile.__len__())
print(len(profile))                 #   Magic Method [__len__] لازم اكون عامل  len() علشان استخدم ال 

# __class__   Used To Know The Intended Instance(object) Is Belongs To any Class?
print(profile.__class__) 
# Not for Only Instance but Also for Objects.
age = 19
print(age.__class__)

# __str__
name = 'Ahmed'
print(type(name))  
print(name.__class__)
print(name.upper())
print(str.upper(name))