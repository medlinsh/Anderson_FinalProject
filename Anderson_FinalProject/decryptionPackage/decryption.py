'''
#Name: Dhenuka Suthaharan, Noah Draper, Jon Buck, Seth Medlin
#email: medlinsh@mail.uc.edu
#Assignment: Final Project
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can decrypt and create a program to show photos
#Citations: N/A
#Anything else thats relevant: N/A
'''

import json

#load the JSON file
with open("C:\\Users\\15137\\Documents\\Fall 2022 Classes\\Advanced App Development\\Final Project\\Final Project Fall 2022-1\\EncryptedGroupHints.json") as json_file:
    data = json.load(json_file)
   
print(type(data))
