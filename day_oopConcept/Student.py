from day_oopConcept.Person import Person

class Student(Person):

    def __init__(self):
        pass

    def __init__(self, firstName, lastName, rollNumber, discipline):
        super().__init__(firstName, lastName)
        self.rollNumber = rollNumber
        self.discipline = discipline

    def getStudentInfo(self):
        return self.fullName() + " " + self.rollNumber + " " + self.discipline

    def display(self):
        self.display();
        print(f"{self.rollNumber} {self.discipline}")


