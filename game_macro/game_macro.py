from selenium import webdriver
import time

path = "C:/chromedriver.exe" 
driver = webdriver.Chrome(path)
driver.get("http://zzzscore.com/1to50/")

cnt = 1
while cnt <= 50:
    num = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
    for n in num:
        if n.text == str(cnt):
            n.click()
            print(str(cnt)+"클릭")
            cnt += 1
            break
