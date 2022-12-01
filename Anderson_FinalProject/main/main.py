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
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO
'''
def load_image( filename ) :
    myimage = Image.open(filename)
    myimage.load()
    
    return myimage
my_image = load_image("IMG_3340.jpg")
my_image.show(my_image)

'''
def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        return None


im = Image.open("main/IMG_3340.jpg")
im_c = im.crop((200,300,400,500)) # (left, top, right, bottom) it's a tuple!
im_c.show()


