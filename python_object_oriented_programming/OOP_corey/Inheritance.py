class Employee:
    raise_amount = 1.04
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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)  # == Employee.__init__(self, fname, lname, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.full_name())


dev_1 = Developer('Ahmed', 'Ghnnam', 50000, 'Python')
dev_2 = Developer('Maram', 'Ahmed', 60000, 'MySQL')

# print(dev_1.email)
# print(dev_2.prog_lang)

# print(help(Developer))

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

mgr_1 = Manager('Lena', 'Ahmed', 45000, [dev_1])

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emp()

print(isinstance(dev_1, Employee))

