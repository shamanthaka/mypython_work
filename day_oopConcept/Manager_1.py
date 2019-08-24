from day_oopConcept.Employee_1 import Employee_1
from day_oop.Developer import Developer

class Manager_1(Employee_1):
    def __init__(self, first_name, last_name, email, pay, employees=None):
        super().__init__(first_name, last_name, email, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

