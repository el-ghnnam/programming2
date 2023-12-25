class Employee:
    raise_amount = 1.05
    num_of_emps = 0

    # set attributes automatically for each instance
    def __init__(self, fname, lname, pay):  # self => refers to instance variable name
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = f"{fname}.{lname}@gmail.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return self.fname + ' ' + self.lname

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):   # cls => refers to class variable name
        cls.raise_amount = amount     # can change cls to class name

    # Automatically
    @classmethod
    def convert_string_to_instance(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)


emp_1 = Employee('Ahmed', 'Ghnnam', 12000)
emp_2 = Employee('Maram', 'Ahmed', 10000)


Employee.set_raise_amt(1.07)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# How to pass emp as string and convert this to emp
# Manually
emp_str_3 = 'Ibrahim-Ahmed-9000'
print(emp_str_3.split('-'))
fname, lname, pay = emp_str_3.split('-')
emp_3 = Employee(fname, lname, pay)

# print(emp_3.full_name())
# print(emp_3.email)
# print(emp_3.pay)
print('-' * 50)

emp_str = 'Lena-Ahmed-8000'
emp_4 = Employee.convert_string_to_instance(emp_str)
print(emp_4.full_name())
print(emp_4.email)
print(emp_4.pay)