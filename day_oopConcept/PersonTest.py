import unittest

from day_oopConcept.Person import Person

class PersonTest(unittest.TestCase):

    def test_fullName(self):
        person = Person("Vinny", "Veerareddy")
        self.assertAlmostEqual(person.fullName(), "Vinny Veerareddy")