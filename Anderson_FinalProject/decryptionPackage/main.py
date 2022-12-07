'''
#Name: Dhenuka Suthaharan, Noah Draper, Jon Buck, Seth Medlin
#email: suthahda@mail.uc.edu, drapernm@mail.uc.edu, buckjn@mail.uc.edu, medlinsh@mail.uc.edu
#Assignment: Final Project
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can decrypt and create a program to show photos
#Citations: N/A
#Anything else thats relevant: N/A
'''
from decryption import *
from PIL import Image

#print decryption
result = decrypt()
print(result)

#Show photo
im = Image.open("group_photo.jpg")
my_image = load_image("group_photo.jpg")

im.show()