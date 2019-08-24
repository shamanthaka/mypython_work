import unittest

from day_oopConcept.Student import Student

class StudentTest(unittest.TestCase):

    def test_get_student_info(self):
        student = Student("Vinny", "Veerareddy", "1234", "Computer Science");
        self.assertAlmostEqual(student.getStudentInfo(),"Vinny Veerareddy 1234 Computer Science")