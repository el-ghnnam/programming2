# Python object-oriented programming


class Employee:
    # set attributes automatically for each instance
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = f"{fname}.{lname}@gmail.com"

    def full_name(self):
        return self.fname + ' ' + self.lname


emp_1 = Employee('Ahmed', 'Ghnnam', 12000)
emp_2 = Employee('Maram', 'Ahmed', 10000)
# add attributes manually to each instance
# emp_1.fname = 'Ahmed'
# emp_1.lname = 'Ghnnam'
# emp_1.email = 'ahmedghnnam@gmail.com'
# emp_1.pay = 12000
#
# emp_2.fname = 'Maram'
# emp_2.lname = 'Ahmed'
# emp_2.email = 'MaramAhmed@gmail.com'
# emp_2.pay = 10000

print(emp_1.email)
print(emp_1.full_name())    # without this parenthesis'()' after the method print return
# the method not the value of the method
print('-' * 50)

# Note this
print(emp_2.full_name())
print(Employee.full_name(emp_2))
