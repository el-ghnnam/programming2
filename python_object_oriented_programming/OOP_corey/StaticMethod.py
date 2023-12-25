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

    @classmethod
    def convert_string_to_instance(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)

    @staticmethod    # don't take argument for instance(self) or for class(cls)
    def is_workday(day):
        # weekday == 3 => Thursday, weekday == 4 => Friday
        if day.weekday() == 3 or day.weekday() == 4:
            return False
        return True


emp_1 = Employee('Ahmed', 'Ghnnam', 12000)
emp_2 = Employee('Maram', 'Ahmed', 10000)

from datetime import date
my_date = date(2003, 12, 10)
print(Employee.is_workday(my_date))