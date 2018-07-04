from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json

otl_url = 'http://www.milliyet.com.tr/abd-bmgk-dan-iran-icin-acil-dunya-2583991/'

#opening up connection and grabbing page
uClient = urlopen(otl_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


data = [] # create a list to store the items
item = {}

temp = page_soup.findAll("div",{"class":"date"})
item['created-edited'] = temp[0].text

temp = page_soup.findAll("h1",{"itemprop":"headline"})
item['headline'] = temp[0].text

temp = page_soup.findAll("h2",{"itemprop":"description"})
item['description'] = temp[0].text

temp = page_soup.findAll("p")
text = []
i = 1
for txt  in temp:
    parafs = {}
    a = "p" + str(i)
    parafs[a] = txt.text
    text.append(parafs)
    i = i +1 
item['text'] = text

temp = page_soup.findAll('img',{"class":"image"})
photo = []
i = 1
for pht  in temp:
    print(pht)
    photos = {}
    a = "img" + str(i)
    photos[a] = pht['src']
    photo.append(photos)
    i = i +1 
item['photo'] = photo

    


data.append(item) # add the item to the list
    


with open("aleyna.json", "w", encoding='utf8') as writeJSON:
    json.dump(data, writeJSON, ensure_ascii=False)