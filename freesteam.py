from bs4 import BeautifulSoup
import requests 
import os


url = "https://freesteam.ru/"


images_path = 'images'

if not os.path.exists(images_path):
         os.mkdir(images_path)

def parse_link():

    result = requests.get(url)
    result = result.content
    
    soup = BeautifulSoup(result, "lxml")

    links = soup.find(class_="col-lg-4 col-md-4 three-columns post-box").find(class_="entry-title").find("a")
    images = soup.find(class_="col-lg-4 col-md-4 three-columns post-box").find(class_="post-thumb").find("img")
    image = images.get("data-src")

    link = links.get("href")
    links = links.text

    f = open(os.path.join(images_path, '00000001.jpg'), 'wb')
    f.write(requests.get(image).content)
    f.close()
    
    return link, links 
    




