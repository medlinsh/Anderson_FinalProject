'''
#Name: Dhenuka Suthaharan, Noah Draper, Jon Buck, Seth Medlin
#email: medlinsh@mail.uc.edu
#Assignment: Final Project
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can decrypt and create a program to show photos
#Citations: https://bobbyhadz.com/blog/python-print-dictionary-line-by-line,
https://stackoverflow.com/questions/8205807/how-to-convert-a-text-file-into-a-list-in-python#8205830
#Anything else thats relevant: N/A
'''

import json

#load the JSON file
with open("EncryptedGroupHints.json") as json_file:
    parseKey = json.load(json_file)   
#print(type(data))
#print(parseKey)


#Analyzing the english file
englishText = open("english.txt",'r') #Reading the file
englishParced = [line.split(',') for line in englishText.readlines()] #storing it as a list



for key in parseKey['Anderson']:
    print(englishParced[int(key)])




#Talked to Professor and he mentioned that the englishparced is list so I ditched this idea
'''
counter = -1

for key in parseKey:    
    for line in englishParced:
        counter += 1
            if key in line
    


#    print(line, counter)
    if str(counter) in parseKey['Anderson']:
        print(line) 
      '''  

