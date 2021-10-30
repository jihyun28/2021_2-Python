# -*- coding: euc-kr -*-

# html ���� ������ �������� ���� ����ϴ� ���̺귯��
import urllib.request
import requests
from bs4 import BeautifulSoup

# �ҷ��� url �ּ� 
web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')

print("*** ���￩�ڴ��б� �а� �� Ȩ������ ���� ***")
print("�а�\t\t\t\t\tȨ������")

dept = soup.find_all("li")

for d in dept:
   
    url = "http://www.swu.ac.kr" + d.a["href"]
    web = urllib.request.urlopen(url)
    soup = BeautifulSoup(web, "html.parser")
    dep = d.a.text

    if ("�а�" in dep) or ("����" in dep):
        if(soup.find('a', {"class":"btn btn_xl btn_blue_gray"})):
            page = soup.find("a", {'class':'btn btn_xl btn_blue_gray'})['href']
            print(f"{d.text}\t\t\t{page}")

    else:
        print("Ȩ�������� �������� ����")