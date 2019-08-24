class Person_1:
    def __init__(self):
        pass
    def __init__(self, firstName, SecondName):
        self.firstName = firstName
        self.SecondName = SecondName

    def fullName(self):
        return self.firstName + " " + self.SecondName

    def display(self):
        print(f"{self.firstName} {self.SecondName}")
