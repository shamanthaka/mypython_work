import unittest

from  day_oopConcept.Student_1 import Student_1

class StudentTest(unittest.TestCase):
    def test_get_student_info(self):
        student = Student_1("vinny", "veerareddy", "1234","computer science");
        self.assertAlmostEqual(student.getStudentInfo(), "vinny veerareddy 1234 computer science")