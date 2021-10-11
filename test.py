#!bin/python3
from selenium import webdriver
import time, requests
import os
from PIL import Image

img_arr = ['dog', 'cat', 'wolf', 'cow', 'youtube', 'green', 'france', 'python', 'art', 'note', 'table', 'crow', 'home depot', 'world cup', 'skeletons', 'pie', 'obama', 'sans', 'smash', 'halloween']
jpg_path = 'images/'
png_path = 'pngs/'
loop_count = 0
DIR = 'supermetroid/' #set to outputname
num_rom = 0
num_images = 0


def search_google(search_query, loop_count):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(options=options)
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
    images_url = []

    # open browser and begin search
    browser.get(search_url)
    elements = browser.find_elements_by_class_name('rg_i')

    count = 0

    for e in elements:
        # get images source url
        e.click()
        time.sleep(1)
        element = browser.find_elements_by_class_name('v4dQwb')

        # Google image web site logic
        if count == 0:
            big_img = element[0].find_element_by_class_name('n3VNCb')
        else:
           big_img = element[1].find_element_by_class_name('n3VNCb')

        images_url.append(big_img.get_attribute("src"))

        # write image to file
        reponse = requests.get(images_url[count])
        if reponse.status_code == 200:
            with open(f"{jpg_path}search{loop_count}.jpg","wb") as file:
                file.write(reponse.content)

        count += 1

        # Stop get and save after 5
        if count == 1:
            break

    return images_url

num_rom = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
print(num_rom)

for i in img_arr:
    items = search_google(i, loop_count)
    loop_count += 1
    if (loop_count >= num_rom): #set to amount of images creatd by merge
        break

num_images = len([name for name in os.listdir(jpg_path) if os.path.isfile(os.path.join(jpg_path, name))])
print(num_images)

for x in range(num_images):
    im = Image.open(f"{jpg_path}search{x}.jpg")
    im.save(f"{png_path}search{x}.png")

