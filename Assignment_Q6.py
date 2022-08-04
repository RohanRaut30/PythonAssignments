'''Python MCA Assignment No. 6 '''

# Q1
from tokenize import Special
from numpy import delete
import pymongo as pm
con = pm.MongoClient("mongodb://localhost:27017/")

mydb = con["HMS"]  # To create Database
mycollection = mydb["Hospital"]  # To create Collection(Table)
mycollection_D = mydb["Doctor"] 

'''data = {'Hostpital_id': 1, 'Hostpital_Name': 'Sassoon Hospital', 'Bed_Count': 1000}
mycollection.insert_one(data)
print("Document inserted!!")'''

#***************************************************************************
# Q2

'''multiData = [
    {'Hostpital_id': 1, 'Hostpital_Name': 'Sassoon Hospital', 'Bed_Count': 10000},
    {'Hostpital_id': 2, 'Hostpital_Name': 'Sahyadri Hospital', 'Bed_Count': 1500},
    {'Hostpital_id': 3, 'Hostpital_Name': 'Kem Hospital', 'Bed_Count': 700},
    {'Hostpital_id': 4, 'Hostpital_Name': 'Pawna Hospital', 'Bed_Count': 2000},
    {'Hostpital_id': 5, 'Hostpital_Name': 'Khandelwal Hospital', 'Bed_Count': 800},
    {'Hostpital_id': 6, 'Hostpital_Name': 'Park Hospital', 'Bed_Count': 6500},
    {'Hostpital_id': 7, 'Hostpital_Name': 'Dhanwantare Hospital', 'Bed_Count': 8400},
    {'Hostpital_id': 8, 'Hostpital_Name': 'Southern Command Hospital', 'Bed_Count': 100},
    {'Hostpital_id': 9, 'Hostpital_Name': 'Indriyani Hospital', 'Bed_Count': 1400},
    {'Hostpital_id': 10, 'Hostpital_Name': 'Leena Hospital', 'Bed_Count': 2600}
]

mycollection.insert_many(multiData)
print("Mulitiple Documents inserted !!!")'''



#******************************************************************************
# Q3

'''prev_val = int(input("Enter Hospital Id:- "))
bed_count = int(input("Enter Bed Count:- "))

prev = {"Hostpital_id":prev_val}
nextt = {"$set":{"Bed_Count":bed_count}}
mycollection.update_one(prev, nextt)
print("Updated Sucessfully!!")'''

#**************************************************************************************
# Q4

'''H_id = int(input("Enter Hospital Id:- "))
toDelete = {"Hostpital_id":H_id}
mycollection.delete_one(toDelete)
print("Record Deleted Succesfully!!")'''

#**************************************************************************
#Q5

'''docs = mycollection.find()
for iteam in docs:
    print(iteam)'''

#**************************************************************************
#Q6

'''version = con.server_info()["version"]
print(version)'''

#**************************************************************************
#Q7
#Douth
'''docs = mycollection.find()
docs1 = mycollection_D.find()
for iteam in docs :
    print(iteam)
for iteam in docs1 :
    print(iteam)
'''
#**************************************************************************
#Q8
# multiData = [
#    {'Doctor_Id': 3, 'Doctor_Name': 'Suraj', 'Hospital_id': 3, 'Joining_Date': '02-08-2002', 'Speciality': 'Dentist', 'Salary': 50000, 'Experience': 7},
#    {'Doctor_Id': 4, 'Doctor_Name': 'Siddharth', 'Hospital_id': 4, 'Joining_Date': '02-08-2012', 'Speciality': 'cardiology', 'Salary': 50000, 'Experience': 7},
#    {'Doctor_Id': 5, 'Doctor_Name': 'Kishor', 'Hospital_id': 5, 'Joining_Date': '02-08-2019', 'Speciality': 'Surgery', 'Salary': 50000, 'Experience': 7},
#    {'Doctor_Id': 6, 'Doctor_Name': 'Omkar', 'Hospital_id': 6, 'Joining_Date': '02-08-2005', 'Speciality': 'cardiology', 'Salary': 50000, 'Experience': 7},
#    {'Doctor_Id': 7, 'Doctor_Name': 'Alwyn', 'Hospital_id': 7, 'Joining_Date': '02-08-2008', 'Speciality': 'Surgery', 'Salary': 50000, 'Experience': 7},
#    {'Doctor_Id': 8, 'Doctor_Name': 'Shreesail', 'Hospital_id': 8, 'Joining_Date': '02-08-2019', 'Speciality': 'Neurology', 'Salary': 50000, 'Experience': 7},
#    {'Doctor_Id': 9, 'Doctor_Name': 'Vaibhav', 'Hospital_id': 9, 'Joining_Date': '02-08-2015', 'Speciality': 'Dentist', 'Salary': 50000, 'Experience': 7},
#    {'Doctor_Id': 10, 'Doctor_Name': 'Sukesh', 'Hospital_id': 10, 'Joining_Date': '02-08-2014', 'Speciality': 'Neurology', 'Salary': 50000, 'Experience': 7}
# ]

# mycollection_D.insert_many(multiData)
# print("Mulitiple Documents inserted !!!")




#**************************************************************************
#Q9









#**************************************************************************
#Q10


'''dName = input("Enter Doctor Name:- ")
yrs = int(input("Update Years of Experience:- "))

Doct = {"Doctor_Name":dName}
Exp = {"$set":{'Experience': yrs}}
mycollection_D.update_one(Doct, Exp)
print("Experience Updated Sucessfully!!")'''



