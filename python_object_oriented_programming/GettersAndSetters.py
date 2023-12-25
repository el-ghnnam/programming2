# --------------------------------------------------------
# -- Object Oriented Programming => Getters And Setters --
# --------------------------------------------------------

class Member:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return f'Name Is {self.__name}'

    def set_name(self, new_name):
        self.__name = new_name
        


member_one = Member('ahmed'.capitalize())
print(member_one.get_name())
Member.set_name(member_one, 'maram')     #  ==  member_one.set_name('maram').
print(Member.get_name(member_one))

