# InfiniDrive w/ OpenStego
Unlimited Cloud Drive using Amazon Prime Photos(I don't think Amazon does unlimited anymore because of r/datahoarders)
The reason I made this fork is because uploading these images to any cloud sharing site like Google or Amazon is very suspicious. This way it shouldn't get flagged by bots as being malware.
Also I added my test.py's because using request wasn't my first attempt at getting random images. So I added these in case anyone needs.
Also if you change the flower search at like 160 for the scraper you can use other images like a dog.

How it's done:
1. The app opens the file you wanna store in RAW binary
2. Bytes of the file are splitted and converted to RGB PNG images
3. Now you are ready to upload all the images to Amazon Prime Photos. As they are images, they are unlimited. You can create an album to download everything at once 
4. Download your album as a zip, then unzip it
5. The app will merge all the images to recreate the original file
6. The magic is done 😎

The recovered file has perfect integrity. Sha256 checksum is passed.


New Feature:
1. Added a -d flag to insert the split images into random images download from Unsplash.
2. The image downloading work is done in imgdl.py
3. Request is made to get data from Unsplash
4. Search term is entered and remaining data is queried and saved to a jpg.
5. Frankly their API does a better job of explaining it.
6. I used openstego in the command line because no python module I could find would accept an image as the thing to hide. Which is just cover file, hidden file, output file in command line.
7. It works the same as InfiniDrive so no need to worry about what file names to enter.

## Installation
Assure that you have python3.8 installed on your system.
```sh
#Clone this repo
git clone https://github.com/nicomda/InfiniDrive

#Install virtualenv if not installed
pip3 install virtualenv

#Creating virtualenv
python3 -m venv InfiniDrive

#Activating venv
source ./bin/activate

#Installing required libraries in the virtual enviroment
pip3 install -r requirements.txt
```

## OpenStego
OpenStego needs to be installed on your system. Follow your distros instructions on how to do so.
[https://www.openstego.com/index.html]

## Quick Start
```bash
#To split a file: 
./InfiniDrive.py -s 'file_to_split'

#To split a file changing size of images. The default size is 2000x2000 (12MB): 
./InfiniDrive.py -s 'file_to_split' --imgpxl=100

#To merge images: 
./InfiniDrive.py -m 'images_folder'
```

### **Available arguments:**

| Argument        | What it does | Optional |
| --------------- |:-------------|:---------:| 
| -s                               |Split mode 
| -m                               |Merge mode 
| -o <new_output_folder>                              |Change default output folder when splitting |✔
| --outputfile=<out_file_path>     |Path where output file will be created |✔
| --imgpxl='side_size'    |Change the size of the output images |✔
| -q                            |OpenStego flag |✔
| -h                            |Extended help |✔

