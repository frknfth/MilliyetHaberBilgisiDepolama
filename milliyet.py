from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json

otl_urlAy = 'http://www.milliyet.com.tr/2018/01/'

dataStep3 =[]
dataStep2 = []

for x in range(1,5):
    sayi22 = 1

    y = ""
    if x<10:
        y = "0" + str(x)
    else:
        y = str(x)

    otl_url = otl_urlAy + y
    uClient = urlopen(otl_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    urls = []
    günSon = []

    temp = page_soup.findAll("a",{"class":"surmanset"})
    for txt  in temp:
        if txt["href"].find("emlak") == -1:
            if txt["href"].find("galeri") == -1:
                if txt["href"].find("milliyetsanat") == -1:
                    if txt["href"].find("teknoloji-haber") == -1:
                        if txt["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt["href"].find("icerik") == -1:
                                if txt["href"].find("blog") == -1:
                                    if txt["href"].find("kariyer.milliyet") == -1:
                                        if txt["href"].find("oyunhaberleri") == -1:
                                            if txt["href"].find("populerbilim") == -1:
                                                if txt["href"].find("trendyol") == -1:
                                                    if txt["href"].find("apple-haber") == -1:
                                                        if txt["href"].find("mobil-haber") == -1:
                                                            urls.append(txt["href"])

    temp = page_soup.findAll("a",{"class":"bigImg"})
    for txt  in temp:
        if txt["href"].find("emlak") == -1:
            if txt["href"].find("galeri") == -1:
                if txt["href"].find("milliyetsanat") == -1:
                    if txt["href"].find("teknoloji-haber") == -1:
                        if txt["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt["href"].find("icerik") == -1:
                                if txt["href"].find("blog") == -1:
                                    if txt["href"].find("kariyer.milliyet") == -1:     
                                        if txt["href"].find("oyunhaberleri") == -1:
                                            if txt["href"].find("populerbilim") == -1:
                                                if txt["href"].find("trendyol") == -1:                                                               
                                                    if txt["href"].find("apple-haber") == -1:
                                                        if txt["href"].find("mobil-haber") == -1:                                                                
                                                            urls.append(txt["href"])

    temp = page_soup.findAll("div",{"class":"img"})
    for txt  in temp:
        if txt.a["href"].find("emlak") == -1:
            if txt.a["href"].find("galeri") == -1:
                if txt.a["href"].find("milliyetsanat") == -1:
                    if txt.a["href"].find("teknoloji-haber") == -1:
                        if txt.a["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt.a["href"].find("icerik") == -1:
                                if txt.a["href"].find("blog") == -1: 
                                    if txt.a["href"].find("kariyer.milliyet") == -1:
                                        if txt.a["href"].find("oyunhaberleri") == -1: 
                                            if txt.a["href"].find("populerbilim") == -1:
                                                if txt.a["href"].find("trendyol") == -1:                                                                     
                                                    if txt.a["href"].find("apple-haber") == -1:
                                                        if txt.a["href"].find("mobil-haber") == -1:                                                                
                                                            urls.append(txt.a["href"])

    temp = page_soup.findAll("div",{"class":"nws3"})
    for txt  in temp:
        if txt.a["href"].find("emlak") == -1:
            if txt.a["href"].find("galeri") == -1:
                if txt.a["href"].find("milliyetsanat") == -1:
                    if txt.a["href"].find("teknoloji-haber") == -1:                                                    
                        if txt.a["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt.a["href"].find("icerik") == -1:
                                if txt.a["href"].find("blog") == -1:  
                                    if txt.a["href"].find("kariyer.milliyet") == -1:  
                                        if txt.a["href"].find("oyunhaberleri") == -1: 
                                            if txt.a["href"].find("populerbilim") == -1:
                                                if txt.a["href"].find("trendyol") == -1:                                                                   
                                                    if txt.a["href"].find("apple-haber") == -1:
                                                        if txt.a["href"].find("mobil-haber") == -1:                                                                
                                                            urls.append(txt.a["href"])

    temp = page_soup.findAll("div",{"class":"fs20"})
    for txt  in temp:
        if txt.a["href"].find("emlak") == -1:
            if txt.a["href"].find("galeri") == -1:
                if txt.a["href"].find("milliyetsanat") == -1:
                    if txt.a["href"].find("teknoloji-haber") == -1:
                        if txt.a["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt.a["href"].find("icerik") == -1:
                                if txt.a["href"].find("blog") == -1:  
                                    if txt.a["href"].find("kariyer.milliyet") == -1:   
                                        if txt.a["href"].find("oyunhaberleri") == -1:
                                            if txt.a["href"].find("populerbilim") == -1:
                                                if txt.a["href"].find("trendyol") == -1:                                                                   
                                                    if txt.a["href"].find("apple-haber") == -1:
                                                        if txt.a["href"].find("mobil-haber") == -1:                                                                
                                                            urls.append(txt.a["href"])
                                            
    temp = page_soup.findAll("div",{"class":"h600"})
    for txt  in temp:
        if txt.a["href"].find("emlak") == -1:
            if txt.a["href"].find("galeri") == -1:
                if txt.a["href"].find("milliyetsanat") == -1:
                    if txt.a["href"].find("teknoloji-haber") == -1:
                        if txt.a["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt.a["href"].find("icerik") == -1:
                                if txt.a["href"].find("blog") == -1:   
                                    if txt.a["href"].find("kariyer.milliyet") == -1:   
                                        if txt.a["href"].find("oyunhaberleri") == -1: 
                                            if txt.a["href"].find("populerbilim") == -1:
                                                if txt.a["href"].find("trendyol") == -1:                                                                 
                                                    if txt.a["href"].find("apple-haber") == -1:
                                                        if txt.a["href"].find("mobil-haber") == -1:                                                                
                                                            urls.append(txt.a["href"])

    temp = page_soup.findAll("div",{"class":"w138"})
    for txt  in temp:
        if txt.a["href"].find("emlak") == -1:
            if txt.a["href"].find("galeri") == -1:
                if txt.a["href"].find("milliyetsanat") == -1:
                    if txt.a["href"].find("teknoloji-haber") == -1:
                        if txt.a["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt.a["href"].find("icerik") == -1:
                                if txt.a["href"].find("blog") == -1:     
                                    if txt.a["href"].find("kariyer.milliyet") == -1: 
                                        if txt.a["href"].find("oyunhaberleri") == -1:
                                            if txt.a["href"].find("populerbilim") == -1: 
                                                if txt.a["href"].find("trendyol") == -1:                                                                 
                                                    if txt.a["href"].find("apple-haber") == -1:
                                                        if txt.a["href"].find("mobil-haber") == -1:                                                                
                                                            urls.append(txt.a["href"])

    temp = page_soup.findAll("div",{"class":"w300"})
    for txt  in temp:
        if txt.a["href"].find("emlak") == -1:
            if txt.a["href"].find("galeri") == -1:
                if txt.a["href"].find("milliyetsanat") == -1:
                    if txt.a["href"].find("teknoloji-haber") == -1:
                        if txt.a["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt.a["href"].find("icerik") == -1:
                                if txt.a["href"].find("blog") == -1:    
                                    if txt.a["href"].find("kariyer.milliyet") == -1:  
                                        if txt.a["href"].find("oyunhaberleri") == -1:
                                            if txt.a["href"].find("populerbilim") == -1: 
                                                if txt.a["href"].find("trendyol") == -1:                                                            
                                                    if txt.a["href"].find("apple-haber") == -1:
                                                        if txt.a["href"].find("mobil-haber") == -1:                                                                
                                                            urls.append(txt.a["href"])

    temp = page_soup.findAll("div",{"class":"wBox"})
    for txt  in temp:
        if txt.a["href"].find("emlak") == -1:
            if txt.a["href"].find("galeri") == -1:
                if txt.a["href"].find("milliyetsanat") == -1:
                    if txt.a["href"].find("teknoloji-haber") == -1:
                        if txt.a["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt.a["href"].find("icerik") == -1:
                                if txt.a["href"].find("blog") == -1:   
                                    if txt.a["href"].find("kariyer.milliyet") == -1:  
                                        if txt.a["href"].find("oyunhaberleri") == -1:
                                            if txt.a["href"].find("populerbilim") == -1:
                                                if txt.a["href"].find("trendyol") == -1:                                                                 
                                                    if txt.a["href"].find("apple-haber") == -1:
                                                        if txt.a["href"].find("mobil-haber") == -1:                                                                
                                                            urls.append(txt.a["href"])
   
    temp = page_soup.findAll("a",{"class":"nwsImg"})
    for txt  in temp:
        if txt["href"].find("emlak") == -1:
            if txt["href"].find("galeri") == -1:
                if txt["href"].find("milliyetsanat") == -1:
                    if txt["href"].find("teknoloji-haber") == -1:
                        if txt["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt["href"].find("icerik") == -1:                                                                        
                                if txt["href"].find("blog") == -1:
                                    if txt["href"].find("kariyer.milliyet") == -1:
                                        if txt["href"].find("oyunhaberleri") == -1:
                                            if txt["href"].find("populerbilim") == -1:
                                                if txt["href"].find("trendyol") == -1:
                                                    if txt["href"].find("apple-haber") == -1:
                                                        if txt["href"].find("mobil-haber") == -1:                                                                
                                                            urls.append(txt["href"])

    temp = page_soup.findAll("a",{"class":"lnk1"})
    for txt  in temp:
        if txt["href"].find("emlak") == -1:
            if txt["href"].find("galeri") == -1:
                if txt["href"].find("milliyetsanat") == -1:
                    if txt["href"].find("teknoloji-haber") == -1:
                        if txt["href"].find("mantoloma-ve-yalitim") == -1:
                            if txt["href"].find("icerik") == -1: 
                                if txt["href"].find("blog") == -1:       
                                    if txt["href"].find("kariyer.milliyet") == -1:  
                                        if txt["href"].find("oyunhaberleri") == -1:
                                            if txt["href"].find("populerbilim") == -1:
                                                if txt["href"].find("trendyol") == -1:                                                             
                                                    if txt["href"].find("apple-haber") == -1:
                                                        if txt["href"].find("mobil-haber") == -1:                                                                
                                                            urls.append(txt["href"])

    for x in urls:
        print(y + " " + str(sayi22) +" "+x)
        sayi22 = sayi22 + 1
            
    data = [] # create a list to store the items

    haberSayisi = 1
    for url in urls:

        try:
            uClient2 = urlopen(url)
            page_html = uClient2.read()
            uClient2.close()

            page_soup = soup(page_html, "html.parser")            

            item = {}
            item["url"] = url

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
                print(pht["alt"])
                photos = {}
                a = "img" + str(i)
                photos[a] = pht['src']
                photo.append(photos)
                i = i +1 
            item['photo'] = photo

            son = {}
            son["newsNumber"] = str(haberSayisi)
            son["newsContent"] = item

            haberSayisi = haberSayisi + 1

            data.append(son) # add the item to the list
    
        except Exception as e:
            continue                

    son = {}
    son["date"] = y + "/01/2018"
    son["data"] = data
    dataStep2.append(son)

dataStep3.append(dataStep2)

with open("store.json", "w", encoding='utf8') as writeJSON:
    json.dump(dataStep3, writeJSON, ensure_ascii=False)    