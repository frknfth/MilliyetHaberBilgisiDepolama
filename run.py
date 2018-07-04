from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json

otl_url = 'https://open.umn.edu/opentextbooks/SearchResults.aspx?subjectAreaId=99'

#opening up connection and grabbing page
uClient = urlopen(otl_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs info for each textbook
containers = page_soup.findAll("div",{"class":"twothird"})

data = [] # create a list to store the items
for container in containers:
    item = {}
    item['title'] = container.h2.text
    item['author'] = container.p.text
    item['link'] = "https://open.umn.edu/opentextbooks/" + container.h2.a["href"]
    data.append(item) # add the item to the list


with open("textbooks.json", "w") as writeJSON:
    json.dump(data, writeJSON, ensure_ascii=False)