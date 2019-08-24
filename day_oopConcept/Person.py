class Person:

    def __init__(self):
        pass

    def __init__(self, firstName, secondName):
        self.firstName = firstName
        self.secondName = secondName

    def fullName(self):
        return self.firstName + " " + self.secondName

    def display(self):
        print(f"{self.firstName} {self.secondName}")

