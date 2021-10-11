#!bin/python3
import requests
import os
from PIL import Image
from os import listdir
from os.path import isfile, join

num_images = 0
png_path = 'pngs/'
jpg_path = 'unsplash/'

class Unsplash:
    def __init__(self,search_term,per_page,quality="full"):
        self.search_term = search_term
        self.per_page = per_page
        #self.page = 0
        self.quality = quality
        #self.headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5", "Host": "unsplash.com", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}
        self.headers ={"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5", "Connection": "keep-alive", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}


    def set_url(self):
        #return f"https://unsplash.com/napi/search/photos?query={self.search_term}&xp=&per_page={self.per_page}&page={self.page}"
        #https://unsplash.com/napi/search?query={self.search_term}&xp=feedback-loop-v2:control&per_page={self.per_page}
        return f"https://unsplash.com/napi/search?query={self.search_term}&per_page={self.per_page}"

    def make_request(self):
        url = self.set_url()
        return requests.request("GET",url,headers=self.headers)

    def get_data(self):
        self.data = self.make_request().json()

    def save_path(self,name):
        download_dir = "unsplash"
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        return f"{os.path.join(os.path.realpath(os.getcwd()),download_dir,name)}.jpg"

    def download(self,url,name):
        filepath = self.save_path(name)
        with open(filepath,"wb") as f:
            f.write(requests.request("GET",url,headers=self.headers).content)

    def Scraper(self,pages):
        for page in range(0,pages+0):
            self.make_request()
            self.get_data()
            for item in self.data['photos']['results']:
                name = item['id']
                url = item['urls'][self.quality]
                print(url)
                self.download(url,name)
            #self.pages += 1

if __name__ == "__main__":
    scraper = Unsplash("flower", 10)
    scraper.Scraper(1)
    num_images = len([name for name in os.listdir(jpg_path) if os.path.isfile(os.path.join(jpg_path, name))])
    print(num_images)
    onlyfiles = [f for f in listdir(jpg_path) if isfile(join(jpg_path, f))]
    print(onlyfiles)
    """for x in range(num_images):
        im = Image.open(f"{jpg_path}search{x}.jpg")
        im.save(f"{png_path}search{x}.png")"""
