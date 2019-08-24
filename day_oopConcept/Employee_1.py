import datetime

from day06.Employee_1 import Employee_1


class Employee_1:
    raise_amount = 2.06
    no_of_employees = 0

    def __init__(self,first_name,last_name, email,pay,):
        self.f1 = first_name
        self.l1 = last_name
        self.e1 = email
        self.p1= pay
        Employee_1.no_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.f1, self.l1)

    def display(self):
        print(self.f1())
        print('{} {}'.format(self.e1,str(self.p1)))

    def apply_amount(self):
        self.p1 = int(self.p1 * Employee_1.raise_amount)

    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    def from_string(cls, emp_str):
        first , last, email, pay = emp_str.split('-')
        return  cls(first, last,email,float(pay))

    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True
    def __repr__(self):
        return "Employee('{}','{}','{}','{}')".format(self.f1, self.l1,self.e1,self.p1)

    def __str__(self):
        return "[{},{}, {}, {}]".format(self.f1,self.l1,self.e1,self.p1)

    def __add__(self, other):
        return self.p1 + other.p1


    if __name__ == '__main__':
        emp1 = Employee_1("Venkatram", "veerareddy","venkat.veerareddy@gmail.com",50000)

        emp2 = Employee_1("Srijan","veerareddy","Srijan.veerareddy@gmail.com",50000)

        print("Adding two employees: " + str(emp1 + emp2))

        print("1.")
        emp1.apply_amount()

        print("2.")
        emp2.display()

        print("3.")
        print(emp1.__dict__)

        Employee_1.set_raise_amount(1.2)
        emp2.apply_amount()
        print("4.")
        emp2.display()

        emp3 = Employee_1.from_string("Winnie-Veerareddy-Winnie.Veerareddy@gmail.com-60000")
        emp3.display()

        print("*******")
        print(emp3)

        my_date = datetime.date(2018, 10, 24)

        print("Is today working day?" +str(Employee_1.is_workday(my_date)))
