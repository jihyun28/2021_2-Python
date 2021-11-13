from bs4 import BeautifulSoup
import urllib.response
import urllib.request
import requests
import os

html = urllib.request.urlopen("https://comic.naver.com/webtoon/list?titleId=769568&weekday=sat")
res = BeautifulSoup(html.read(), "html.parser")

search = res.find("div",{"class", "detail"})
title = search.find("h2").get_text()
title2 = search.find("span").get_text()
title = title.replace(title2, "")

title = title.strip()
print(title)

os.mkdir(title)
os.chdir(title)

search = res.findAll("td", {"class", "title"})
epi_list=[]
epi_url=[]

index = 0
for e in search:
    epi_list.append(e.get_text(" ", strip = True))
    epi_url.append(e.find("a").get('href'))
    os.mkdir(epi_list[index])
    index += 1

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safaari/537.36')]
urllib.request.install_opener(opener)

epi = 0
for u in epi_url:
    src_list=[]
    image_list=[]
    html = urllib.request.urlopen("https://comic.naver.com" + u)
    res = BeautifulSoup(html.read(), "html.parser")
    search = res.findAll("img")

    for s in search:
        src_list.append(s.get('src'))

    for i in range(0, len(src_list), 1):
        text = "image-comic"
        src_string = str(src_list[i])
        if text in src_string:
            image_list.append(src_list[i])
        index += 1

    index = 1
    for i in image_list:
        path = epi_list[epi] + "/"
        urllib.request.urlretrieve(i, path+str(index) + ".jpg")
        index += 1
    epi += 1