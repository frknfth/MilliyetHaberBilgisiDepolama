from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json
import datetime
from pprint import pprint
otl_urlAy = 'http://www.milliyet.com.tr/2018/'

dataStep2 = []




with open('store.json', encoding='utf-8') as f:
    data = json.load(f)

try:
    for f in range(0,500000):
        temp = []
        son = {}
        son["date"] = data["allTheNews"][f]["date"]
        son["theNewsOfTheDay"] = data["allTheNews"][f]["theNewsOfTheDay"]

        dataStep2.append(son)
except Exception as e:
    pass


allDayArray = []
try:
    for f in range(0,500000):
        allDayArray.append(str(data["allTheNews"][f]["date"]))
except Exception as e:
    pass


for f in allDayArray:
    print(f)



for y in range(1,13):

    month =""
    if y <10:
        month = "0"+ str(y) + "/"
    else:
        month = str(y) + "/"
    
    otl_urlDay = otl_urlAy + month



    for x in range(1,33):
        sayi22 = 1

        day = ""
        if x<10:
            day = "0" + str(x)
        else:
            day = str(x)

        otl_url = otl_urlDay + day

        print(otl_url)
        try:
            abc =True
            for f in allDayArray:
                if day + "/" + month + "2018" in f:
                    abc = False
                    print(abc)
                    break

            if(abc == True):
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
                    print(day + " " + str(sayi22) +" "+x)
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

                        allDatesHours = temp[0].text.split("                    ")

                        item['createdDay'] = allDatesHours[0]
                        item['createdHour'] = allDatesHours[1]
                        item['lastEditDay'] = str(allDatesHours[2])[str(allDatesHours[2]).find(":")+1:str(allDatesHours[2]).find("-")]
                        item['lastEditHour'] =str(allDatesHours[2])[str(allDatesHours[2]).find("-")+1:str(allDatesHours[2]).rfind(" ")]

                        date1 = str(item['createdDay']) + " " + str(item['createdHour']) 

                        datetimeFormat = '%d.%m.%Y %H:%M' 

                        date2 = str(item['lastEditDay']) + " " + str(item['lastEditHour']) 


                        date11 = datetime.datetime.strptime(date1, datetimeFormat)

                        date12 = datetime.datetime.strptime(date2,datetimeFormat)

                        diff = date12 - date11

                        days = diff.days
                                                                                              
                        minutes = (diff.seconds) / 60

                        item['MinuteDiffBetweenDaysHours'] = str(minutes)



                        temp = page_soup.findAll("h1",{"itemprop":"headline"})
                        item['headline'] = temp[0].text

                        temp = page_soup.findAll("h2",{"itemprop":"description"})
                        item['description'] = temp[0].text

                        temp = page_soup.findAll("p")
                        text = ""
                        for txt  in temp:
                            parafs = ""
                            parafs = txt.text
                            text +=parafs
                        item['text'] = text

                        temp = page_soup.findAll('img',{"class":"image"})

                        print(temp[0]["alt"])

                        photos = ""
                        photos = temp[0]['src']

                        item['photo'] = photos

                        
                        etiket= []
                        productDivs = page_soup.findAll('div',{"class":"etiket"})

                        for anA in productDivs[0].find_all("a"):
                            Biretiket ={}
                            Biretiket = anA.text
                            etiket.append(Biretiket)

                        item['tags'] = etiket


                        productDivs = page_soup.findAll('div',{"class":"em2"})

                        Biretiket ={}
                        Biretiket["happy"] =        productDivs[0].find_all("span")[0].text
                        Biretiket["confused"] =     productDivs[0].find_all("span")[1].text
                        Biretiket["irresulate"] =   productDivs[0].find_all("span")[2].text
                        Biretiket["mad"] =          productDivs[0].find_all("span")[3].text
                        Biretiket["sad"] =          productDivs[0].find_all("span")[4].text

                        Biretiket["totalVote"] =    str(int(productDivs[0].find_all("span")[0].text) + int(productDivs[0].find_all("span")[1].text) + int(productDivs[0].find_all("span")[2].text) + int(productDivs[0].find_all("span")[3].text) + int(productDivs[0].find_all("span")[4].text))

                        item['statements'] = Biretiket



                        haberSayisi = haberSayisi + 1

                        data.append(item) # add the item to the list
                
                    except Exception as e:
                        print(e)                

                son = {}
                son["date"] = day + "/" + month + "2018"
                son["theNewsOfTheDay"] = data
                dataStep2.append(son)
        except Exception as e:
            print(e)
        


lastJson = {}
lastJson["web_site"] = "www.milliyet.com.tr"
lastJson["allTheNews"] = dataStep2



with open("store.json", "w", encoding='utf8') as writeJSON:
    json.dump(lastJson, writeJSON, ensure_ascii=False)    
