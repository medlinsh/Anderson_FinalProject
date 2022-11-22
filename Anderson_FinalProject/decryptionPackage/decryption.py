'''
#Name: Dhenuka Suthaharan, Noah Draper, Jon Buck, Seth Medlin
#email: medlinsh@mail.uc.edu
#Assignment: Final Project
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can decrypt and create a program to show photos
#Citations: https://bobbyhadz.com/blog/python-print-dictionary-line-by-line
#Anything else thats relevant: N/A
'''

import json

#load the JSON file
with open("EncryptedGroupHints.json") as json_file:
    data = json.load(json_file)
   
print(type(data))

text = open("english.txt",'r').readlines()
print(type(text))

for line, value in data.items():
    print(line, value)
    
