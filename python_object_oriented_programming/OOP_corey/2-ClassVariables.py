class Employee:
    raise_amount = 1.05
    num_of_emps = 0

    # set attributes automatically for each instance
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = f"{fname}.{lname}@gmail.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return self.fname + ' ' + self.lname

    def display_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)
emp_1 = Employee('Ahmed', 'Ghnnam', 12000)
emp_2 = Employee('Maram', 'Ahmed', 10000)
print(Employee.num_of_emps)

emp_1.display_raise()
print(emp_1.pay)
print('-' * 50)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('-' * 50)

print(emp_1.__dict__)
print('-' * 50)

emp_1.raise_amount = 1.06
print(emp_1.raise_amount)
print(emp_1.__dict__)  # because he modified the raise_amount this variable becomes a part of this dict
print('-' * 50)
