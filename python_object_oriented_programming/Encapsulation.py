# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------

# Restrict Access To The Data Sorted in Attirbutes And Methods.
# Public.
#       Every Attirubtes And Methods Are We Used So Far Is Public.
#       Attirubtes And Methods Can Be Modified And Run In EveryWhere.
#       Inside Our Outside The Class.
# Protected.
#        Attirubtes And Methods Can Be Accessed From Within The Class And Sud Class(Derived classes).
#        Attirubtes And Methods Prefixed With One Underscore [ _ ].
#        Attirbutes Can Be Modified From Outside The Class.
# Private.
#        Attirubtes And Methods Can Be Accessed From Within The Class Or Object Only.
#        Attirbutes Can't Be Modified From Outside The Class, But Can Be Access Inside The Class.
#        Attirubtes And Methods Prefixed With Two Underscore [ __ ].
# --------------------------------------------------------------------------------
# --- Attirbutes == Variables == Properties --- .
# --------------------------------------------------------------------------------

class Member:
    def __init__(self, name_one, name_two, name_three):
        self.name_one = name_one
        self._name_two = name_two
        self.__name_three = name_three

    def say_hello(self):
        return f' Hello {self.__name_three}'


# Public.
member_one = Member('ibrahim', 'ahmed', 'maram')
print(member_one.name_one)

member_one._name = 'Maram'
print(member_one.name_one)
# ---------------------------------------------

# Protected.   # But Not Supported In Python.
member_two = Member('ibrahim', 'ahmed', 'maram')
print(member_two._name_two)

member_two._name = 'Maram'
print(member_two._name_two)
# ----------------------------------------------

# Private.
member_three = Member('ibrahim', 'ahmed', 'maram')
# print(member_three.__name_three)     # error
print(member_three._Member__name_three)     # 2

member_three._Member__name_three = 'Maram'
# print(member_three.__name_three)     # error
print(member_three._Member__name_three)     # 1

# 1,2  Are Wrong Way To Modified The Private Attirbutes.
# The Best Way To Do This By Using Getter And Setter.

# To Access Inside The Class 
# 1- Make A Function
print(Member.say_hello(member_three))
# -- or -- 
print(member_three.say_hello())
# ----------------------------------------------
