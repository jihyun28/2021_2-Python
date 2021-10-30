# -*- coding: euc-kr -*-

# html 문서 정보를 가져오기 위해 사용하는 라이브러리
import urllib.request
from bs4 import BeautifulSoup

# 불러올 url 주소 
web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')

print("*** 서울여자대학교 학과 및 홈페이지 정보 ***")
print("학과\t\t\t\t\t홈페이지")

dept = soup.find_all("li")

for d in dept:
   
    url = "http://www.swu.ac.kr" + d.a["href"]
    web = urllib.request.urlopen(url)
    soup = BeautifulSoup(web, "html.parser")
    dep = d.a.text

    if ("학과" in dep) or ("전공" in dep) or ("학부" in dep):
        if(soup.find('a', {"class":"btn btn_xl btn_blue_gray"})):
            page = soup.find("a", {'class':'btn btn_xl btn_blue_gray'})['href']
            print(f"{d.text}\t\t\t{page}")
        else:
            print("홈페이지가 존재하지 않음")

    else:
        print("홈페이지가 존재하지 않음")
