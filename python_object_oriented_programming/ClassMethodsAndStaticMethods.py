# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# -- Required You To Put The (cls) prammeter
# -- cls => Point To The Class Methods
# -- Marked With @classmethod Decorator To Flag It As Class Method
# -- It Take (forced) Cls Parameter Not Self To Point To The Class not The Instance
# -- It Doesn't Require a Creation of Class Instance
# -- Used when You Want To Do Something With The Class Itself
# Static Methods:
# -- It Takes No Parameters
# -- It's Bound To The Class Not Instance(Creates From Class)
# -- Used When Doing Something Doesn't Have Access To Object or Class But Only Related To Class
# ----------------------------------------------------------------------------

class Member:

    NotAllowedNames = ['Fuck', 'Shit', 'Damn', 'Hell']
    NumberOfUsers = 0

    @classmethod
    def ShowUsersCount(cls):
        print(f'We Have {cls.NumberOfUsers} Members In Our System')

    @staticmethod
    def SayHello():
        print('Say Hello From Static Method')

    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Member.NumberOfUsers += 1

    def get_full_name(self):
        if self.fname in Member.NotAllowedNames:
            raise ValueError('Name Not Allowed')
        else:
            return f'{self.fname} {self.mname} {self.lname}'
    def say_Hello(self):
        if self.fname in Member.NotAllowedNames:
            raise ValueError('Name Not Allowed')
        if self.gender == 'Male':
            return f'Hello Mr {self.fname}'
        elif  self.gender == 'Female' :
            return f' Hello Ms {self.fname}'
    def get_all_info(self):
        if self.fname in Member.NotAllowedNames:
            raise ValueError('Name Not Allowed')
        else:
            return f'{self.say_Hello()}, Your Full Name Is  {self.get_full_name()}'
    def DeleteUser(self):
        Member.NumberOfUsers -= 1
        return f'User {self.fname} Deleted. '

print(Member.NumberOfUsers)

member_1 = Member('ahmed', 'Ibrahim', 'Ghnnam', 'Male')
member_2 = Member('Maram', 'Ahmed', 'Ghnnam', 'Female')
member_3 = Member('Ibrahim', 'Ahmed', 'Ghnnam', 'Male')
print(Member.NumberOfUsers)

# print(member_1.say_Hello())
# print(member_2.get_all_info())
# print(member_1.say_Hello())
# print(dir(Member))
# ----------------------------------------------------
# print(member_3.DeleteUser())
# print(f'Now Number Of User is {Member.NumberOfUsers}')
# ----------------------------------------------------
# To Run The Class Methods
Member.ShowUsersCount()  # or print(Member.ShowUsersCount) but Without print are better than with print.
# ----------------------------------------------------
# If You want To Run Any Instance Like [member_2] with Instance Method called get_full_name()
print(member_2.get_full_name())  
# In Python Bakcground This Happen To What You Want
print(Member.get_full_name(member_2))
# ----------------------------------------------------
# Run Static Methods Like Run Class Method
Member.SayHello()
# ----------------------------------------------------
