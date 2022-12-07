'''
#Name: Dhenuka Suthaharan, Noah Draper, Jon Buck, Seth Medlin
#email: suthahda@mail.uc.edu, drapernm@mail.uc.edu, buckjn@mail.uc.edu, medlinsh@mail.uc.edu
#Assignment: Final Project
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can decrypt and create a program to show photos
#Citations: https://bobbyhadz.com/blog/python-print-dictionary-line-by-line,
https://stackoverflow.com/questions/8205807/how-to-convert-a-text-file-into-a-list-in-python#8205830,
https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/,
https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
#Anything else thats relevant: N/A
'''

import json
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO


def decrypt():
    #load the JSON file
    with open("EncryptedGroupHints.json") as json_file:
        parseKey = json.load(json_file)   
    #print(type(data))
    #print(parseKey)


    #Analyzing the english file
    englishText = open("english.txt",'r') #Reading the file
    englishParced = [line.split(',') for line in englishText.readlines()] #storing it as a list


    #selects the 'Anderson' list in the parseKey dictionary
    for key in parseKey['Anderson']:
    
        print(englishParced[int(key)]) #prints/calls the entity for the given numerical entry (key) 

    
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

def load_image( filename ) :
    try: 
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        return None
   
    
    
    

