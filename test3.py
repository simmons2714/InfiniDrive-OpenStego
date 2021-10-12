#!bin/python3
import os
from PIL import Image
from os import listdir
from os.path import isfile, join
from imgdl import Unsplash
import LSBSteg as lsb
import base64
import cv2

#encode
with open("supermetroid_0.png", "rb") as image2string:
    converted_string = base64.b64encode(image2string.read())

with open('encode.bin', "wb") as file:
    file.write(converted_string)

steg = lsb.LSBSteg(cv2.imread("YdAqiUkUoWA.png"))
data = open("encode.bin", "rb").read()
new_img = steg.encode_binary(data)
cv2.imwrite("new_image.png", new_img)

#decode
steg = lsb.LSBSteg(cv2.imread("new_image.png"))
binary = steg.decode_binary()
with open("recovered.bin", "rb") as f:
    f.write(data)

file = open('recovered.bin', 'rb')
byte = file.read()
file.close()

decodeit = open('hello_level.png', 'wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()
