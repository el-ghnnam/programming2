# --------------------------------------------------------------------
# Instance == Object
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes are exist (Define) Inside The Constructor(__init__)
# -------------------------------------------------------------------------
# Instance Methods: Take self Parameter Which Point To Instance Created From Class
# Instance Methods Required You To Put (slef) Parameter
# Instance Methods can Have More Than One Parameter Like Any Function
# Instance Methods can Freely Access Attributes And Methods On The Same Object
# Instance Methods can Access The Class Itself
# -------------------------------------------------------------------

class Member:
    def __init__(self, first_name, middle_name, last_name):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        
member_one = Member("Ahmed", "Ibrahim", "Ghnnam")
member_two = Member("Maram", "Ahmed", "Ghnnam")
print(member_two.fname, end = ' ')
print(member_two.mname, end = ' ')
print(member_two.lname)
print(member_one.fname, member_one.mname, member_one.lname)
print("-" * 40)


