#!bin/python3
import os
from PIL import Image
from os import listdir
from os.path import isfile, join
from imgdl import Unsplash
import subprocess

#png_path = 'pngs/'
jpg_path = 'unsplash/'
rom_path = 'supermetroid/' # change to get path
stego_path = 'stegofiles/'

if not os.path.exists(stego_path):
    os.mkdir(stego_path)

scraper = Unsplash("flower", 2)# set to number of images made
scraper.Scraper(1)

num_images = len([name for name in os.listdir(jpg_path) if os.path.isfile(os.path.join(jpg_path, name))])
onlyfiles = [f for f in listdir(jpg_path) if isfile(join(jpg_path, f))]

#old thing for when stego wanted png's
"""for x in onlyfiles:
    im = Image.open(f"{jpg_path}{x}")
    im.save(f"{png_path}{x.split('.')[0]}.png")"""

#onlyfiles_png = [f for f in listdir(png_path) if isfile(join(png_path, f))]
onlyfiles_rom = [f for f in listdir(rom_path) if isfile(join(rom_path, f))]

for i, token in enumerate(onlyfiles_rom):
    #print(token)
    #print(onlyfiles_png[i])
    command = f"openstego embed -mf {rom_path}{token} -cf {jpg_path}{onlyfiles[i]} -sf {stego_path}file{i}.png"
    subprocess.call(command, shell=True)

onlyfiles_stego = [f for f in listdir(stego_path) if isfile(join(stego_path, f))]
print(onlyfiles_stego)

#openstego embed -mf supermetroid_0.png -cf B_SLtmXPKNA.jpg -sf test.png

#command = f"openstego embed -mf {rom_path}{onlyfiles_rom[0]} -cf {jpg_path}{onlyfiles[0]} -sf {stego_path}file{i}.png"
#subprocess.call(command, shell=True)
