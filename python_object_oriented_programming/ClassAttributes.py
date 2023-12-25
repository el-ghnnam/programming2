# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# -- Class Attributes: Attributes Defined OutSide The Constructor --
# ------------------------------------------------------------------


class Member:

    NotAllowedNames = ['Fuck', 'Shit', 'Damn', 'Hell']
    NumberOfUsers = 0

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
print(member_3.DeleteUser())
print(f'Now Number Of User is {Member.NumberOfUsers}')