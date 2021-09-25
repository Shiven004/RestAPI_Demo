"""
Description: This module invokes read process to fetch lab data 
             and perform different fetch operations based on below scenarios:
                 1. Fetch lab centre data based on lab id
                 2. Generate patient id and associate lab centre booked.


Author:     Shivender Khajuria           
Dated:      25-09-21
Filename:   fetch_data_op.py
Version:    1.0
Purpose:    Wipro Tech Test

"""
from read_write_op import read_lab_details
import random

def fetch_lab_details(lab_id):    
    lab_centre_details = []
    lab_data = read_lab_details()
    for lab in lab_data:        
        if lab['lab_id'] == lab_id:
            lab_centre_details.append(lab)
    return lab_centre_details

def gen_patient_details(lab_id,test_requested):
    lab_centre_details = fetch_lab_details(lab_id)    
    patient_data = {}
    # Generate unique patient_id for the patient.
    if  lab_centre_details:
        patient_id = "PAT_" + lab_id +"_" + str(random.randint(1111,9999))
        patient_data["Patient_ID"] = patient_id  
    #fetch details from lab_centre_details list.
    for item in lab_centre_details:        
        patient_data["Lab_ID"] = item["lab_id"]
        patient_data["Lab_Type"] = item["lab_type"]
        patient_data["Test_Name"] = test_requested     
    return patient_data