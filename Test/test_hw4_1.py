import unittest
import re

class Patient:
    def __init__(self, name, symptoms):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not all(isinstance(symptom, str) for symptom in symptoms):
            raise TypeError("Symptoms must be a list of strings")
        self.name = name
        self.symptoms = symptoms
        self.tests = {}

    def add_test(self, name_of_the_test, results):
        if not isinstance(name_of_the_test, str):
            raise TypeError("Name must be a string")
        if not isinstance(results, bool):
            raise TypeError("Results must be a boolean")
        self.tests[name_of_the_test] = results

    def has_covid(self):
        for test_name, test_result in self.tests.items():
                if re.search(r'covid', test_name, re.IGNORECASE):
                    if test_result == True:
                        return 0.99
                    else:
                        return 0.01
        symptom_count = sum(symptom in self.symptoms for symptom in ['fever', 'cough', 'anosmia'])
        return 0.05 + 0.1 * symptom_count

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
        patient.add_test("COVID Test", 0.01)

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