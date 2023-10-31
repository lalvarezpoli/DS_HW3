import unittest
import re
import hw4
from hw4 import Patient

class test_PatientMethods(unittest.TestCase):

    def test_has_covid_with_test_results(self):
        # Test case where test for COVID is available and positive
        patient = Patient("TestPatient", ["fever", "cough"])
        patient.add_test("COVID Test", True)
        self.assertEqual(patient.has_covid(), 0.99)

    def test_has_symptoms_without_test_results(self):
        # Test case where test for COVID is not available
        patient = Patient("TestPatient", ["fever", "cough"])
        self.assertEqual(patient.has_covid(), 0.25)  # Assuming no COVID test

    def test_has_covid_with_negative_test(self):
        # Test case where test for COVID is available but negative
        patient = Patient("TestPatient", ["fever", "cough"])
        patient.add_test("Covid", False)
        self.assertEqual(patient.has_covid(), 0.01) 

    def test_has_covid_without_symptoms(self):
        # Test case where the patient has no symptoms
        patient = Patient("TestPatient", [])
        self.assertEqual(patient.has_covid(), 0.05)

    def test_has_covid_without_any_tests(self):
        # Test case where no tests are conducted but with symptoms
        patient = Patient("TestPatient", ["fever", "cough"])
        self.assertEqual(patient.has_covid(), 0.25)  # Assuming no COVID test

    def test_has_covid_with_other_tests(self):
        # Test case where tests are conducted but not for COVID
        patient = Patient("TestPatient", ["fever", "cough"])
        patient.add_test("Blood Test", False)
        patient.add_test("X-Ray", True)
        self.assertEqual(patient.has_covid(), 0.25)  # Assuming no COVID test

    def test_no_covid_with_other_tests(self):
        # Test case where tests are conducted but not for COVID
        patient = Patient("TestPatient", [])
        patient.add_test("Blood Test", False)
        patient.add_test("X-Ray", True)
        self.assertEqual(patient.has_covid(), 0.05)  # Assuming no COVID test

    def test_covid_badly_written(self):
        # Test case where tests are conducted but not for COVID
        patient = Patient("TestPatient", [])
        patient.add_test("Covid2020", True)
        patient.add_test("X-Ray", True)
        self.assertEqual(patient.has_covid(), 0.99)  # Assuming no COVID test
    
if __name__ == '__main__':
    unittest.main()
