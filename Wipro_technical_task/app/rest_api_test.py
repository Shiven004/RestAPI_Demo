"""
Decription: This is a pytest utility to perform unit testing for Small Lab Rest API functions and data.
Author:     Shivender Khajuria           
Dated:      26-09-21
Filename:   rest_api_test.py
Version:    1.0
Purpose:    Wipro Tech Test

"""
# Import libraries here.
import unittest
from fetch_data_op import fetch_lab_details, gen_patient_details
from main import app
from fastapi.testclient import TestClient

# Tests adapted from `problem-specifications/lab_centres.json`
lab_lst = [{'lab_id': 'A1001', 'index': 1, 'lab_type': 'G', 'email': 'a1001@xyz.com', 'phone': '+1 (123) 567-3630', 
            'address': 'Craigieburn, 3063', 'postal_code': 3063, 'about': 'Craigieburn General Test Lab Centre.\r\n', 
            'registered': '2016-07-13T12:29:07 -10:00', 'tests_available': ['Liver Function Test', 'Blood Test',
             'TSH Thyroid Test', 'Random Blood Sugar Test']}]

client = TestClient(app)

class RestApi_UnitTest(unittest.TestCase):    

    def test_empty_list(self):
        self.assertListEqual(fetch_lab_details([]), [])        
    
    def test_fetch_lab_data_with_valid_lab_id(self):
        self.assertListEqual(fetch_lab_details(lab_id="A1001"), lab_lst)
    
    def test_fetch_lab_data_with_invalid_lab_id(self):
        self.assertListEqual(fetch_lab_details("ABC123"), [])    
    
    def test_gen_patient_details_invalid_data(self):
        self.assertDictEqual(gen_patient_details("ABC1230", "Blood Test"), {})
    
    def test_read_lab_details_valid(lab_id = "A1001"):
        response = client.get("/lab/A1001")
        assert response.status_code == 200
        assert response.json() == {"Lab Centre Details": lab_lst}

    def test_read_lab_details_invalid(lab_id = "A1008"):
        response = client.get("/lab/A1008")
        assert response.status_code == 404
        assert response.json() == {'detail': 'Lab details not found...'}
