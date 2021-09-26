"""
Description: This module reads the data from json files present in data directory
             and perform different fetch operations based on below scenarios.             

Author:     Shivender Khajuria           
Dated:      25-09-21
Filename:   read_write_op.py
Version:    1.0
Purpose:    Wipro Tech Test

"""
#Import libraries here.
import json 

#Global variables.
dir_path = '../app/data/'
filename_lab_data = 'lab_centres.json'
filename_patient = 'patient_details.json'


# Funtion performs read operations on the lab_centres.json.
def read_lab_details():
    print("Performing read operation - input order details now....")
    #Orders details json deserialize operation.
    with open(dir_path + filename_lab_data, "r") as read_file:
        try:                  
            lab_details  = json.load(read_file)
        except:
            print("Please check orders_details.json file format....\n")
            read_file.seek(0)
            lab_details = json.loads('['+read_file.read().replace('}{','},{')+']')[0]
        finally:
            print("Exiting read_orders_details process now...")   
    return lab_details


# Funtion performs write operation on lab_response_data.json.
def write_patient_details(patient_details):
    print("Performing write operation - unique orders now....")
    #Orders details json deserialize operation.
    with open(dir_path + filename_patient, "a+") as write_file:
        try:                  
            json.dump(patient_details, write_file, indent=4)            
        except IOError:
            print("Error while writing to unique_orders.json file....\n")
        finally:
            print("Exiting write_unique_details process now...")           
    return
