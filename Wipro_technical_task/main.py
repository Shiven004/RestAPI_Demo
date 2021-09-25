"""
Decription: This utility is based on fastapi FastAPI is a modern, 
            fast (high-performance), web framework for building APIs with Python 3.6+ 
            based on standard Python type hints.
            Following scenerios have been covered in this script:-
                1. A REST API endpoint.
                2. Running POST or PUT to this endpoint runs an asynchronous task.

Author:     Shivender Khajuria           
Dated:      25-09-21
Filename:   main.py
Version:    1.0
Purpose:    Wipro Tech Test

"""
# Import libraries here.
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from read_write_op import read_lab_details, write_patient_details
from fetch_data_op import fetch_lab_details, gen_patient_details

app = FastAPI()

@app.get("/")
def read_root():
    return {"Wipro": "Technical Task- Please enter relevant lab_id to get lab details"}

#GET Enndpoint: To fetch the lab associated with the lab_id.
@app.get("/lab/{lab_id}")
async def read_lab_details(lab_id: str):
    lab_details_list = fetch_lab_details(lab_id)
    json_lab_details_list = jsonable_encoder(lab_details_list)      
    if len(json_lab_details_list) <= 0:
            raise HTTPException(status_code=404,detail="Lab details not found...")   
    return {"Lab Centre Details": json_lab_details_list}

#Reqmt_02: To get personal information of two people
@app.post("/patient_details/")
async def create_patient_details(lab_id: str, test_requested: str):
    patient_details = gen_patient_details(lab_id, test_requested)
    # Calling Write operation to store patient data.
    write_patient_details(patient_details)
    json_patient_details = jsonable_encoder(patient_details)    
    # Check for Inavlid patient data  
    if len(patient_details) <= 0:
            raise HTTPException(status_code=404,detail="Patient details not found...")   
    return {"Patient Details Added/Updated are": json_patient_details}