class Employee:
    def __init__(self, fname: str, lname: str):  # self => refers to instance variable name
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname, self.lname)

    @property
    def full_name(self):
        return self.fname + ' ' + self.lname

    @full_name.setter
    def full_name(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    @full_name.deleter
    def full_name(self):
        print('Name Deleted!')
        self.fname = None
        self.lname = None


emp_1 = Employee('Ahmed', 'Ghnnam')
emp_1.full_name = 'Maram ghnnam'

print(emp_1.fname)
print(emp_1.email)
print(emp_1.full_name)

del emp_1.full_name
