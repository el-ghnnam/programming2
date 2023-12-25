# --------------------------------------------------------------------
# Instance == Object
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes are exist (Define) Inside The Constructor
# -------------------------------------------------------------------------
# Instance Methods: Take self Parameter Which Point To Instance Created From Class
# Instance Methods can Have More Than One Parameter Like Any Function
# Instance Methods can Freely Access Attributes And Methods On The Same Object
# Instance Methods can Access The Class Itself
# -------------------------------------------------------------------

class Member:
    def __init__(self, first_name, middle_name, last_name, Gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = Gender

    def get_full_name(self):
        return f'{self.fname} {self.mname} {self.lname}'

    def say_hello(self):
        if self.gender == "Male":
            return f'Hello Mr {self.fname}'
        elif self.gender == "Female":
            return f'Hello Miss {self.fname}'
        else:
            return f'{self.fname}'
    def get_all_info(self):
        return f'{self.say_hello()}, Your name Is: {self.get_full_name()}'


member_1 = Member('Ahmed', 'Ibrahim', 'Ghnnam', 'Male')
member_2 = Member('Maram', 'Ahmed', 'Ghnnam', 'Female')

# print(member_1.get_full_name())
# print(member_2.get_full_name())
# print(member_1.say_hello())
# print(member_2.say_hello())
print(member_2.get_all_info())
