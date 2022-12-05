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
from decryption import *

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
from io import BytesIO

result = decrypt()
print(result)

im = load_image("IMG_3340.png")
im.show()

